import sqlite3
import zipfile
import io
from typing import List, Dict, Union

def parse_anki_deck(deck_path: str, deck_format: str = 'apkg') -> List[Dict[str, Union[str, int]]]:
    deck_data = []

    if deck_format == 'apkg':
        with zipfile.ZipFile(deck_path, 'r') as apkg_file:
            # Check if the required files are present in the .apkg
            if 'collection.anki2' not in apkg_file.namelist() or 'lib/libsqlanki.py' not in apkg_file.namelist():
                raise ValueError("Invalid Anki package file. Required files missing.")

            # Load the SQLite database and extension
            sql_file = apkg_file.read('collection.anki2')
            conn = sqlite3.connect(':memory:')
            conn.enable_load_extension(True)
            conn.execute("SELECT load_extension(?)", (apkg_file.read('lib/libsqlanki.py'),))
            conn.executescript(sql_file)
            cursor = conn.cursor()

            # Query the cards table to get the card data
            cursor.execute("SELECT id, question, answer FROM cards")
            rows = cursor.fetchall()
            for row in rows:
                card_id, question, answer = row
                deck_data.append({
                    'id': card_id,
                    'question': question,
                    'answer': answer
                })
            conn.close()

    return deck_data