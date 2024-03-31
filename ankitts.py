import argparse
from gtts import gTTS
from anki_utils import extract_apkg, parse_apkg
from pydub import AudioSegment
import os

def generate_audio(deck_path, output_file):
    db_path = "./data"
    extract_apkg(deck_path, db_path)

    db_path = os.path.join(db_path, 'collection.anki21')
    deck_data = parse_apkg(db_path)
    combined_text = ""

    for card in deck_data:
        combined_text += f"Question: {card['question']}\n\n"
        combined_text += f"Answer: {card['answer']}\n\n"

    tts = gTTS(text=combined_text, lang='en')
    tts.save(output_file)

    # Optional: Merge separate audio files into one
    audio_segments = [AudioSegment.from_file(output_file, format="mp3")]
    combined_audio = AudioSegment.empty()

    for segment in audio_segments:
        combined_audio += segment

    combined_audio.export(output_file, format="mp3")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert Anki deck to audio')
    parser.add_argument('deck_path', type=str, help='Path to Anki deck file')
    parser.add_argument('output_file', type=str, help='Output file for combined audio')
    args = parser.parse_args()

    generate_audio(args.deck_path, args.output_file)