import scipy.io.wavfile as wavfile
import numpy as np
import vlc
import time

distance = -1
while distance < 0:
    try:
        distance = int(input("Enter reflector distance: "))
    except:
        continue
delay = 2*distance / 343 #seconds of delay

print(f'Distance: {distance}m, Delay: {delay}s')

samplingRate, signal = wavfile.read("peterpiper.wav")
#crunch signal to values in [-1, 1]
signal2 = signal.astype(float) / 2**15

delayedSamples = round(delay * samplingRate)
signalWithZeros = np.zeros(delayedSamples)

#Vor und nach der Audio warten, bzw weiterlaufen lassen -> Zeitverschiebung
#Die 2 zeilen -> Gleiche Länge der Arrays
delayedSignal = np.concatenate((signalWithZeros, signal2))
signal2 = np.concatenate((signal2, signalWithZeros))

totalSignal = signal2 + delayedSignal

wavfile.write("echo1.mp3", samplingRate, totalSignal)

p = vlc.MediaPlayer("echo.mp3")
p.play()
time.sleep(10) #Otherwise program finishes before the sound is played