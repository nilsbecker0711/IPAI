import webvtt
from google.cloud import speech_v1
from google.cloud import storage
from google.cloud.speech_v1 import types
import scipy.io.wavfile as wavfile
import io
import wave
import time
import os
import sys

def recognize():
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'Google.json'
    client = speech_v1.SpeechClient()
    encoding = types.RecognitionConfig.AudioEncoding.LINEAR16
    config = {
        "enable_word_time_offsets": True,
        "enable_automatic_punctuation": True,
        "sample_rate_hertz": 16000,
        "language_code": "en-US",
        "encoding": encoding
    }
    audio = {"uri": "gs://vtt0711/subtitles.wav"}
    with open("subtitles.wav","rb") as wav:
        contents = wav.read()
        #audio = {"content":contents}
    print(type(config))
    operation = client.long_running_recognize(audio = audio, config=config)
    response = operation.result()

    textVTT = []
    for result in response.results:
        alternative = result.alternatives[0]

        start = time.strftime('%H:%M:%S', time.gmtime(alternative.words[0].start_time.seconds))
        #startMS = int(alternative.words[0].start_time.nanos/1000000)
        startMS= 0

        end = time.strftime('%H:%M:%S', time.gmtime(alternative.words[-1].end_time.seconds))
        #endMS = int(alternative.words[-1].end_time.nanos/1000000)
        endMS= 0

        textVTT.append(u"{},{} --> {},{}\n{}\n\n".format(start,startMS,end,endMS,alternative.transcript.strip()))
    print(textVTT)
    return textVTT

def printVTT(vtt):
    print([entry for entry in vtt])

samplingRate, signal = wavfile.read("subtitles.wav")
recognize()
