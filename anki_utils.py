import sqlite3
import os
import zipfile
from typing import List, Dict

def qa_has_media(text: str) -> bool:
    if "<img src=" in text:
        return True
    return False

def extract_apkg(apkg_path: str, output_dir: str) -> None:
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Extract contents of the .apkg file
    with zipfile.ZipFile(apkg_path, 'r') as zip_ref:
        zip_ref.extractall(output_dir)

def parse_apkg(db_path: str) -> List[Dict[str, str]]:
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    # Retrieve question-answer pairs from the 'notes' table
    cursor.execute("SELECT flds FROM notes")
    question_answer_pairs = cursor.fetchall()

    # Extract question and answer from the field data
    parsed_data = []
    for pair in question_answer_pairs:
        fields = pair[0].split('\x1f')  # Anki uses the null character as a field separator
        question = fields[0].replace("<br>", " ")
        answer = fields[1].replace("<br>", " ")

        if not qa_has_media(question) and not qa_has_media(answer):
            parsed_data.append({'question': question, 'answer': answer})

    connection.close()

    return parsed_data

