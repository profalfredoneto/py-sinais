from pydub import AudioSegment

song_name = ""

sound_stereo = AudioSegment.from_file(song_name, format="mp3")
sound_monoL = sound_stereo.split_to_mono()[0]
sound_monoR = sound_stereo.split_to_mono()[1]
sound_monoR_inv = sound_monoR.invert_phase()
sound_CentersOut = sound_monoL.overlay(sound_monoR_inv)
fh = sound_CentersOut.export("new_audio.mp3", format="mp3")