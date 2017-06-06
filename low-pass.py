from pydub import AudioSegment
from pydub.playback import play
from matplotlib import pyplot as plt
from matplotlib import mlab
from scipy.fftpack import fft, rfft, irfft, fftfreq
from scipy.io import wavfile
import pylab as pl
import numpy as np
import sys


if __name__ == '__main__':
    if len(sys.argv) != 2:
        if len(sys.argv) < 2:
            print('Too few arguments')
        else:
            print('Too many arguments')

        print('>>> Use: python3 low-pass.py <song_name>\n')
        exit(-1)


    song_name = sys.argv[1]
    fs, data = wavfile.read(song_name)  # fs - sample frequency
    duration = len(data)/fs


    # Low pass  -----------

    print('low-pass filtering')

    signal = np.divide(data.T[0], 2**16)

    W = fftfreq(signal.size, d=1/fs)
    f_signal = rfft(signal)

    # If our original signal time was in seconds, this is now in Hz
    cut_f_signal = f_signal.copy()
    cut_f_signal[(W > 400)] = 0
    #cut_f_signal[(W < 400)] = 0

    cut_signal = irfft(cut_f_signal)

    print('saving filtered signal (low-pass)')
    wavfile.write('teste_lowpass.wav', rate=fs, data=cut_signal)


    # Spec plot  -------------

    plt.figure(1, figsize=(13, 6))
    Pxx, freqs, bins, im = plt.specgram(np.absolute(signal), Fs=fs, NFFT=2048, cmap=plt.get_cmap('CMRmap'),
                                        mode='magnitude', vmin=0, window=mlab.window_hanning, noverlap=900)
    cbar = plt.colorbar(im)
    plt.title('Audio Specgram of ' + song_name)
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency (Hz)')
    cbar.set_label('Intensity (dB)')
    plt.axis([0, duration, 0, 5000])
    #plt.show()

    print('Saving spec_pre-lowpass_' + song_name + '.png')
    plt.savefig('/home/johannes/Documentos/py-sinais/spec_pre-lowpass_' + song_name + '.png', dpi = 200)
    print('spec_pre-lowpass_' + song_name + '.png SAVED!')
    plt.close(1)


    # Spec plot lowpass  -------------

    plt.figure(2, figsize=(13, 6))
    Pxx, freqs, bins, im = plt.specgram(np.absolute(cut_signal), Fs=fs, NFFT=2048, cmap=plt.get_cmap('CMRmap'),
                                        mode='magnitude', vmin=0, window=mlab.window_hanning, noverlap=900)
    cbar = plt.colorbar(im)
    plt.title('Audio Specgram of ' + song_name + 'filtered')
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency (Hz)')
    cbar.set_label('Intensity (dB)')
    plt.axis([0, duration, 0, 5000])
    #plt.show()

    print('Saving spec_lowpass_' + song_name + '.png')
    plt.savefig('/home/johannes/Documentos/py-sinais/spec_lowpass_' + song_name + '.png', dpi = 200)
    print('spec_lowpass_' + song_name + '.png SAVED!')
    plt.close(2)