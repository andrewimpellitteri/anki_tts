# Anki TTS

Anki TTS is a command-line tool that converts an Anki deck into an audio file using text-to-speech (TTS) technology. This tool allows you to create audio versions of your Anki decks, which can be helpful for studying on-the-go or for auditory learners.

## Prerequisites

Before using Anki TTS, make sure you have the following dependencies installed:

- Python 3.x
- `gTTS` library (Google Text-to-Speech)
- `pydub` library (for audio manipulation)

You can install the required libraries using pip:

```
pip install gTTS pydub
```


## Usage

```
python ankitts.py /path/to/your/anki/deck.apkg output.mp3
```

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- [Anki](https://apps.ankiweb.net/) for the amazing spaced repetition software
- [gTTS](https://github.com/pndurette/gTTS) for the Google Text-to-Speech library
- [pydub](https://github.com/jiaaro/pydub) for the audio manipulation library