"""
Main file of the project.
"""


from image2speech_te import audio, ocr, tts


def main(argv: list[str]) -> int:
    """
    Entry point for the application.
    """

    # Get the path to the input image and output audio files.
    image_path = argv[1]
    audio_path = argv[2]

    text = ocr.read_text_from_image(image_path)
    tts.convert_text_to_speech_audio(text, audio_path)
    audio.play_speech_audio(audio_path)

    return 0


if __name__ == "__main__":
    import sys

    sys.exit(main(sys.argv))
