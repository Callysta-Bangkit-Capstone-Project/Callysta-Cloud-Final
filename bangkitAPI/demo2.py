from flask import Flask, jsonify, request
import io
from google.oauth2 import service_account
from google.cloud import speech
from pydub import AudioSegment

app = Flask(__name__)

# Convert audio content to mono
def convert_to_mono(audio_content):
    audio = AudioSegment.from_file(io.BytesIO(audio_content))
    audio = audio.set_channels(1)
    mono_audio_file = io.BytesIO()
    audio.export(mono_audio_file, format='wav')
    mono_audio_content = mono_audio_file.getvalue()
    return mono_audio_content

# Load the speech project service account credentials
client_file = 'speech.json'
credentials = service_account.Credentials.from_service_account_file(client_file)

# Create the Speech-to-Text client
client = speech.SpeechClient(credentials=credentials)

@app.route('/api/speech-to-text', methods=['POST'])
def speech_to_text():
    # Check if audio file is provided
    if 'audio' not in request.files:
        return jsonify({'error': 'No audio file provided'}), 400

    # Get the audio file from the request
    audio_file = request.files['audio']
    audio_content = audio_file.read()

    # Convert audio content to mono
    mono_audio_content = convert_to_mono(audio_content)

    # Load the audio content
    audio = speech.RecognitionAudio(content=mono_audio_content)

    # Configure the recognition
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code='id-ID'
    )

    # Perform the speech recognition
    response = client.recognize(config=config, audio=audio)

    # Get the transcriptions from the response
    transcriptions = []
    for result in response.results:
        transcription = result.alternatives[0].transcript
        transcriptions.append(transcription)

    # Return the transcriptions as JSON
    return jsonify({'transcriptions': transcriptions})

if __name__ == '__main__':
    app.run(debug=True)
