from pydub import AudioSegment
from pydub.playback import play
from matplotlib import pyplot as plt
from matplotlib import mlab
from scipy.fftpack import fft
from scipy.io import wavfile
import pylab as pl
import numpy as np
import sys


song_name = "cocoon.mp3"
cut_name = song_name.split('.mp3')[0] + "-cut.wav"
color = ['b', 'g', 'r']

song = AudioSegment.from_mp3(song_name)
song = song[:60e3:]
song.export(cut_name, format="wav")


if __name__ == '__main__':
    song_name = sys.argv[1]
    fs, data = wavfile.read(song_name)  # fs - sample frequency
    duration = len(data)/fs

    track = {'l':[], 'r':[]}  # Dual channel
    fourier = {'l':[], 'r':[]}  # Signal in frequency
    time = []
    freq = []


    track['l'] = data.T[0]
    track['r'] = data.T[1]
    # this is 16-bit track, b is now normalized on [-1,1)
    track['l'] = np.divide(track['l'], 2**16.)
    track['r'] = np.divide(track['r'], 2**16.)
    #track[i] = [(x/2**16.) for x in track[i]]
    time = np.arange(0., float(len(data)), 1.0)/fs
    # calculate fourier transform (complex numbers list)
    fourier['l'] = fft(track['l'])
    fourier['l'] = np.absolute(fourier['l'][:int(len(fourier['l'])/2-1)])
    fourier['r'] = fft(track['r'])
    fourier['r'] = np.absolute(fourier['r'][:int(len(fourier['r'])/2-1)])


    # Plot Amp/time  -------------------

    f, pltarr = plt.subplots(2, sharex=True, figsize=(16, 9))
    pltarr[0].set_title('Left channel')
    pltarr[0].plot(time, track['l'], linewidth=0.5, alpha=0.7, color='r')
    pltarr[0].set_ylabel('Amplitude')
    pltarr[0].axis([0, duration, -1, 1])
    pltarr[0].grid()

    pltarr[1].set_title('Right channel')
    pltarr[1].plot(time, track['r'], linewidth=0.5, alpha=0.7, color='b')
    pltarr[1].set_ylabel('Amplitude')
    pltarr[1].axis([0, duration, -1, 1])
    pltarr[1].grid()

    plt.xlabel('Time (s)')
    #plt.show()
    print('Saving time-amp_' + song_name + '.png')
    plt.savefig('/home/johannes/Documentos/py-sinais/time-amp_' + song_name + '.png', dpi = 200)
    print('time-amp_' + song_name + '.png SAVED!')


    # Plot dB/Hz  ------------------

    freq = np.arange(0., len(fourier['l']), 1.0)/duration
    f, pltarr = plt.subplots(2, sharex=True, figsize=(16, 9))
    pltarr[0].set_title('Left channel')
    pltarr[0].loglog(freq, fourier['l'], basex=10, basey=10, linewidth=0.5, alpha=0.7, color='r')
    pltarr[0].set_ylabel('Power (dB)')
    pltarr[0].axis([1, 22e3, -10e2, 10e4])
    pltarr[0].grid()

    pltarr[1].set_title('Right channel')
    pltarr[1].loglog(freq, fourier['r'], basex=10, basey=10, linewidth=0.5, alpha=0.7, color='b')
    pltarr[1].set_ylabel('Power (dB)')
    pltarr[1].axis([1, 22e3, -10e2, 10e4])
    pltarr[1].grid()

    plt.xlabel('Frequency (Hz)')
    #plt.show()
    print('Saving freq-power_' + song_name + '.png')
    plt.savefig('/home/johannes/Documentos/py-sinais/freq-power_' + song_name + '.png', dpi = 200)
    print('freq-power_' + song_name + '.png SAVED!')


    # Plot Specgram  ----------------

    plt.figure(3, figsize=(13, 6))
    Pxx, freqs, bins, im = plt.specgram(np.absolute(track['l']), Fs=fs, NFFT=2048, cmap=plt.cm.copper, mode='magnitude',
                                        vmin=0, window=mlab.window_hanning, noverlap=900)
    cbar = plt.colorbar(im)
    plt.title('Audio Specgram Frequecy X Time X Intensity')
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency (Hz)')
    cbar.set_label('Intensity (dB)')
    plt.axis([0, duration, 0, 5000])
    #plt.show()
    print('Saving spec_' + song_name + '.png')
    plt.savefig('/home/johannes/Documentos/py-sinais/spec_' + song_name + '.png', dpi = 200)
    print('spec_' + song_name + '.png SAVED!')