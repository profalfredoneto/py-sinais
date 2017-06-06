from pydub import AudioSegment
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        if len(sys.argv) < 2:
            print('Too few arguments')
        else:
            print('Too many arguments')

        print('>>> Use: python3 convert-wav.py <mp3_song>\n')
        exit(-1)

    song_name = sys.argv[1]
    song = AudioSegment.from_file(song_name, format="mp3")
    song.export(song_name + ".wav", format="wav")
