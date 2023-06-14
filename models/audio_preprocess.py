# preprocess/audio_processing.py
import io
from pydub import AudioSegment

def convert_to_mono(audio_file):
    audio = AudioSegment.from_wav(audio_file)

    # Set channels to 1 (mono)
    audio = audio.set_channels(1)

    # Export audio as bytes
    output = io.BytesIO()
    audio.export(output, format='wav')
    output.seek(0)

    return output
