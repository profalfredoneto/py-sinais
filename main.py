from pydub import AudioSegment
from pydub.playback import play
from matplotlib import pyplot as plt
from matplotlib import mlab
from scipy.fftpack import fft
from scipy.io import wavfile
import pylab as pl
import numpy as np


song_name = "cocoon.mp3"
cut_name = song_name.split('.mp3')[0] + "-cut.wav"
color = ['b', 'g', 'r']

song = AudioSegment.from_mp3(song_name)
song = song[:60e3:]
song.export(cut_name, format="wav")


if __name__ == '__main__':
    fs, data = wavfile.read('cocoon.wav')  # fs - sample frequency
    duration = len(data)/fs

    track = [[], []]  # Dual channel
    fourier = [[], []]  # Signal in frequency
    time = [[], []]
    freq = [[], []]


    for i in range(len(track)):
        track[i] = data.T[i]
        # this is 16-bit track, b is now normalized on [-1,1)
        track[i] = np.divide(track[i], 2**16.)
        #track[i] = [(x/2**16.) for x in track[i]]
        time[i] = np.arange(0., float(len(track[i])), 1.0)/fs
        # calculate fourier transform (complex numbers list)
        fourier[i] = fft(track[i])
        fourier[i] = np.absolute(fourier[i][:int(len(fourier[i])/2-1)])


        # Plot Amp/time  -------------------

        plt.figure(1, figsize=(18, 5))
        plt.plot(time[i], track[i], linewidth=0.03, alpha=0.7, color=color[i])
        plt.title('Amplitude X Time')
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
        plt.axis([0, duration, -1, 1])
        plt.grid()
        plt.show()


        # Plot dB/Hz  ------------------

        plt.figure(2, figsize=(16, 5))
        freq[i] = np.arange(0., len(fourier[i]), 1.0)/duration
        plt.loglog(freq[i], fourier[i], basex=10, basey=10,
                   linewidth=0.03, alpha=0.7, color=color[i])
        plt.title('Power X Frequecy (loglog base 10)')
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Intensity (dB)')
        plt.axis([1, 22e3, 0, 10e5])
        plt.grid()
        plt.show()


        # Plot Specgram  ----------------

        #x = [y*len(data)*64 for y in track[i]]
        plt.figure(3, figsize=(13, 6))
        Pxx, freqs, bins, im = plt.specgram(np.absolute(track[i]), Fs=fs, NFFT=1024, cmap=plt.cm.gist_heat, mode='magnitude',
                                            vmin=0, window=mlab.window_hanning, noverlap=900)
        cbar = plt.colorbar(im)
        plt.title('Audio Specgram Frequecy X Time X Intensity')
        plt.xlabel('Time (s)')
        plt.ylabel('Frequency (Hz)')
        cbar.set_label('Intensity (dB)')
        plt.show()
