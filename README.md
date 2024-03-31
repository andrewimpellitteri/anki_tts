# anki_tts
Utility to convert Anki decks into audio

Sure, here's a good README.md file for your Anki TTS project on GitHub:

# Anki TTS

Anki TTS is a command-line tool that converts an Anki deck into an audio file using text-to-speech (TTS) technology. This tool allows you to create audio versions of your Anki decks, which can be helpful for studying on-the-go or for auditory learners.

## Features

- Supports both plain text files and Anki package (`.apkg`) files as input
- Generates a single audio file (MP3) containing the questions and answers from the Anki deck
- Includes support for handling different text formats and encoding

## Prerequisites

Before using Anki TTS, make sure you have the following dependencies installed:

- Python 3.x
- `gTTS` library (Google Text-to-Speech)
- `pydub` library (for audio manipulation)

You can install the required libraries using pip:

```
pip install gTTS pydub
```

Additionally, if you plan to work with Anki package files (`.apkg`), you'll need to have the `libsqlanki.py` file from the Anki source code in the same directory as your script. This file is required to read the proprietary SQLite database format used by Anki.

## Usage

1. Clone or download the Anki TTS repository.
2. Navigate to the project directory.
3. Run the script with the following command:

```
python ankitts.py /path/to/your/anki/deck.txt output.mp3
```

Or, if you're using an Anki package file:

```
python ankitts.py /path/to/your/anki/deck.apkg output.mp3
```

Replace `/path/to/your/anki/deck.txt` or `/path/to/your/anki/deck.apkg` with the actual path to your Anki deck file (plain text or Anki package file), and `output.mp3` with the desired name and path for the output audio file.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- [Anki](https://apps.ankiweb.net/) for the amazing spaced repetition software
- [gTTS](https://github.com/pndurette/gTTS) for the Google Text-to-Speech library
- [pydub](https://github.com/jiaaro/pydub) for the audio manipulation library