"""
Main file of the project.
"""

import logging
import os

from image2speech_te import audio, ocr, tts


def main(_argv: list[str]) -> int:
    """
    Entry point for the application.
    """

    IMAGE_PATH = "tests/assets/img"
    AUDIO_PATH = "tests/target/aud"

    AUDIO_EXT = ".mp3"
    image_names = os.listdir(IMAGE_PATH)

    if not os.path.exists(AUDIO_PATH):
        os.makedirs(AUDIO_PATH)

    for image_name in image_names:
        audio_name = f"{image_name}{AUDIO_EXT}"

        image_path = os.path.join(IMAGE_PATH, image_name)
        audio_path = os.path.join(AUDIO_PATH, audio_name)

        try:
            text = ocr.read_text_from_image(image_path)
            tts.convert_text_to_speech_audio(text, audio_path)
            audio.play_speech_audio(audio_path)

        except Exception as e:
            logging.error(e)

    return 0


if __name__ == "__main__":
    import sys

    sys.exit(main(sys.argv))
