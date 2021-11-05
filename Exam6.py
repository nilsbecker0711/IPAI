#Author: Nils Wilhelm Becker

import pyaudio
import numpy as np

def playChord(duration, frequency, volume = 1, samplingRate = 44100, minor = False):

    '''
    This method generates and plays a chord based on the "base note". Therefore it calulates first of all the frequencies of the other
    two notes in the chord. Then these 3 frequencies are converted into waves. At last the combination of these waves will be played
    using pyaudio.
    :param duration: float value representing the amount of seconds the chord should be played
    :param frequency: float value representing the frequency of the "base note" of the chord
    :param volume: float value bewteen 0 and 1 representing the volume of the cord to be played. Default 1 -> 100% 
    :param samplingRate: int representing the sampling rate in hertz of the chord to be played. Default 44100
    :param minor: boolean indicating if the chord to be played is a minor chord. If True, the "middle note" of the chord will be different
                  Default False
    '''

    fs = samplingRate      
    duration = duration 
    volume = volume 
    f = frequency       
    f2 = f
    f3 = f
    #update frequencies for middle and top note
    if minor:
        for x in range(1,3):
            f2 = f2 * 2.0**(1/12)
    else:
        for x in range(1,5):
            f2 = f2 * 2.0**(1/12)
    for x in range(1,8):
        f3 = f3 * 2.0**(1/12)
    
    #generate waves for given frequencies
    base = (np.sin(2*np.pi*np.arange(fs*duration*3.5)*f/fs)).astype(np.float32)     #base
    middle = (np.sin(2*np.pi*np.arange(fs*duration*3.5)*f2/fs)).astype(np.float32)  #middle
    top = (np.sin(2*np.pi*np.arange(fs*duration*3.5)*f3/fs)).astype(np.float32)     #top

    p = pyaudio.PyAudio()
    player = p.open(format=pyaudio.paFloat32, channels=1, rate=fs, output=True)

    chord = base + middle + top
    
    chord = chord / np.max(chord) #removes distortion

    # Use next 3 lines to add some melody to the chords :D
    #player.write(volume * base)
    #player.write(volume * middle)
    #player.write(volume * top)

    player.write(volume * chord) 


if __name__ == '__main__':
    #Part 1 -> A major chord A = 440Hz

    playChord(2, 440)


    #Part B -> Melody: “C G Am F G C” (Note Frequencies from: https://pages.mtu.edu/~suits/notefreqs.html)
    c = 261.63
    g = 392
    a = 440
    f = 349.23
    dur = 0.5
    playChord(dur, c)
    playChord(dur, g)
    playChord(dur, a, minor = True)
    playChord(dur, f)
    playChord(dur, g)
    playChord(dur, c)
  