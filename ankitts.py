import argparse
from gtts import gTTS
from anki_utils import extract_apkg, parse_apkg
from pydub import AudioSegment
import os

def generate_audio(deck_path, output_file, pause_duration=2000) -> None:
    db_path = "./data"
    extract_apkg(deck_path, db_path)
    db_path = os.path.join(db_path, 'collection.anki21')
    deck_data = parse_apkg(db_path)

    combined_audio = AudioSegment.empty()

    for card in deck_data:
        question_text = f"Question: {card['question']}"
        answer_text = f"Answer: {card['answer']}"

        # Generate audio for question
        tts = gTTS(text=question_text, lang='en')
        question_audio_file = "temp_question.mp3"
        tts.save(question_audio_file)
        question_audio = AudioSegment.from_file(question_audio_file, format="mp3")
        os.remove(question_audio_file)

        # Generate audio for answer
        tts = gTTS(text=answer_text, lang='en')
        answer_audio_file = "temp_answer.mp3"
        tts.save(answer_audio_file)
        answer_audio = AudioSegment.from_file(answer_audio_file, format="mp3")
        os.remove(answer_audio_file)

        # Combine question, pause, and answer
        combined_audio += question_audio
        combined_audio += AudioSegment.silent(duration=pause_duration)
        combined_audio += answer_audio

    combined_audio.export(output_file, format="mp3")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert Anki deck to audio')
    parser.add_argument('deck_path', type=str, help='Path to Anki deck file')
    parser.add_argument('output_file', type=str, help='Output file for combined audio')
    parser.add_argument('--pause', type=int, default=2000, help='Duration of pause between question and answer (in milliseconds)')
    args = parser.parse_args()
    generate_audio(args.deck_path, args.output_file, args.pause)