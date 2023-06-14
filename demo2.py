from flask import Flask, jsonify, request
import io
from google.oauth2 import service_account
from google.cloud import speech
from pydub import AudioSegment
import os

app = Flask(__name__)

# Convert audio file to mono
def convert_to_mono(audio_file):
    audio = AudioSegment.from_wav(audio_file)

    # Set channels to 1 (mono)
    audio = audio.set_channels(1)

    # Export audio as bytes
    output = io.BytesIO()
    audio.export(output, format='wav')
    output.seek(0)

    return output

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

    # Load the mono audio file
    mono_audio = convert_to_mono(audio_file)

    # Read the content of the mono audio file
    content = mono_audio.read()
    mono_audio.seek(0)

    # Create RecognitionAudio object from the content
    audio = speech.RecognitionAudio(content=content)

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