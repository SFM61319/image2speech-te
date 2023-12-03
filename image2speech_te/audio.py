"""
Audio Module, provides functionality to play speech audio on the device.
"""


import sounddevice as sd
import soundfile as sf


def play_speech_audio(audio_path: str) -> None:
    """
    Plays an audio file using sounddevice.

    Args:
        audio_path: The path to the audio file to play.
    """

    # Load the audio file.
    data, fs = sf.read(audio_path)

    # Play the audio file.
    sd.play(data, fs)
