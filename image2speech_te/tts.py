"""
TTS Module, provides functionality to convert text to speech and save the
speech as an audio file.
"""


import gtts


def convert_text_to_speech_audio(text: str, output_path: str) -> None:
    """
    Converts the text to speech and saves the audio to the output path.

    Args:
        text: The text to convert to speech.
        output_path: The path to save the audio to.
    """

    # Create a gTTS object.
    tts = gtts.gTTS(text, lang="te")

    # Save the audio file.
    tts.save(output_path)
