import numpy as np


class HieuUng:
    def echo(self, audio, delay_time=0.5, decay=0.5):
        delay_samples = int(delay_time * audio.sr)
        decay_filter = np.zeros(len(audio.a))
        decay_filter[delay_samples:] = decay ** np.arange(len(audio.a) - delay_samples)
        echo_audio = audio.a + decay_filter * np.roll(audio.a, delay_samples)
        return echo_audio

    def reversal(self, audio):
        reversed_audio = np.flip(audio.a)
        return reversed_audio

    def dangle(self, audio, dangle_factor=0.1):
        angles = np.exp(1j * np.random.uniform(-dangle_factor * np.pi, dangle_factor * np.pi, size=len(audio.a)))
        dangled_audio = audio.a * angles
        return dangled_audio

    def fade_in(self, audio, fade_duration=1.0):
        fade_in_data = audio.a
        fade_samples = int(fade_duration * audio.sr)
        fade_in_filter = np.linspace(0, 1, fade_samples)
        fade_in_data[:fade_samples] = audio.a[:fade_samples] * fade_in_filter
        return fade_in_data

    def fade_out(self, audio, fade_duration=1.0):
        fade_out_data = audio.a
        fade_samples = int(fade_duration * audio.sr)
        fade_out_filter = np.linspace(1, 0, fade_samples)
        fade_out_data[-fade_samples:] = audio.a[-fade_samples:] * fade_out_filter
        return fade_out_data

    def modulation(self, audio, mod_freq=2.0):
        mod_waveform = np.sin(2 * np.pi * mod_freq * np.arange(len(audio.a)) / audio.sr)
        modulated_audio = audio.a * mod_waveform
        return modulated_audio

