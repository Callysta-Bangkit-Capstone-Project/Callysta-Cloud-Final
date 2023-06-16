import io
from pydub import AudioSegment
from pydub.effects import normalize

def convert_to_mono(audio_file):
    audio = AudioSegment.from_wav(audio_file)

    # Normalize audio
    audio = normalize(audio)

    # Set channels to match the original audio
    num_channels = audio.channels

    # Export audio as bytes with the original number of channels
    output = io.BytesIO()
    audio.export(output, format='wav')
    output.seek(0)

    return output
