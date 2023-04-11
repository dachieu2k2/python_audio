import soundfile as sf
import numpy as np
# from playsound import playsound

class Audio:
    def __init__(self, path):

        self.path = path

        # read file wav
        audio_data, sample_rate = sf.read(path)

        # convert to array
        audio_vector = audio_data.flatten()

        # property
        self.a = np.array(audio_vector)
        self.sr = sample_rate

        # backup neu can
        self.amThanhGoc = np.array(audio_vector)

        # Tần số của file âm thanh
        self.freq = self.sr / len(self.a) 
    def thayDoiKichThuoc (self, audio):
        # thay doi khich thuoc giong audio khac
        self.a = np.resize(self.a, audio.a.shape)
    


    

    