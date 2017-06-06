from pydub import AudioSegment
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        exit(-1)

    song_name = sys.argv[1]
    song = AudioSegment.from_file(song_name, format="mp3")
    song.export(song_name + ".wav", format="wav")
