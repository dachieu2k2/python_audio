import numpy as np
from scipy import signal,fftpack


class TinhToan:
    def TichHaiVector (self,a,b):
        # Tích hai vector âm thanh
        audio_mul = np.multiply(a.a, b.a)
        print("Kết quả tích hai vector âm thanh\n",audio_mul)
        return audio_mul
    
    def TongHaiVector (self,a,b):
        # Tổng hai vector âm thanh
        audio_add = np.add(a.a,b.a)
        print("Kết quả tổng hai vector âm thanh\n",audio_add)
        return audio_add

    def ThuongHaiVector(self,a,b):
        # Thương hai vector âm thanh
        audio_div = np.divide(a.a,b.a)
        print("Kết quả thương hai vector âm thanh\n",audio_div)
        return audio_div
    
    def HieuHaiVector(self,a,b):
        # Hiệu hai vector âm thanh
        audio_sup = np.subtract(a.a,b.a)
        print("Kết quả hiệu hai vector âm thanh\n",audio_sup)
        return audio_sup
    
    def NhanChapVector(self,a,b):
        # Nén để nhân chập và nhân tương quan
        # compressed_audio1 = signal.resample(a.a, len(a.a)//100000)
        # compressed_audio2 = signal.resample(b.a, len(b.a)//100000)
       # Nhân chập
        audio_conv = np.convolve(a.a, b.a,mode='full')
        print("Kết quả nhân chập âm thanh\n",audio_conv)
        return audio_conv
    
    def NhanTuongQuan(self,a,b):
        # compressed_audio1 = signal.resample(a.a, len(a.a)//100000)
        # compressed_audio2 = signal.resample(b.a, len(b.a)//100000)
        # Nhân tương quan
        audio_cor = np.correlate(a.a, b.a,mode='full')
        print("Nhân tương quan âm thanh\n",audio_cor)
        return audio_cor
    
    def DichThoiGian(self,a,s):
        # Tính toán độ dịch tương ứng với thời gian dịch
        samples_shift = int(s * a.sr)

        # Dịch thời gian tín hiệu âm thanh
        shifted_audio_data = np.roll(a.a, samples_shift)

        return shifted_audio_data
    
    def DaoThoiGian(self,a):

        # Tạo mảng thời gian tương ứng với tín hiệu âm thanh
        time_array = np.arange(0, len(a.a)) / a.sr

        # Đảo ngược thời gian
        data_reversed = a.a[::-1]

        # Tạo mảng thời gian tương ứng với tín hiệu âm thanh đảo ngược thời gian
        time_array_reversed = np.arange(0, len(data_reversed)) / a.sr

        return data_reversed 

    def CongSuatNangLuong(self,a):

        area = len(a.a) # diện tích khu vực phát âm thanh
        freq = a.freq # tần số của âm thanh

        # tính toán công suất năng lượng
        power = np.sum(np.square(a.a)) * area * freq

        # in kết quả
        print("Công suất năng lượng của mảng tần số âm thanh là: ", power, "W")
        return power
    
    def KiemTraNhanQua(self,a,b):
        # kiểm tra tính nhân quả của mảng âm thanh
        # Tính hàm tự tương quan

        # compressed_audio1 = signal.resample(a.a, len(a.a)//100000)
        # compressed_audio2 = signal.resample(b.a, len(b.a)//100000)
        auto_corr = np.correlate(a.a,b.a, mode='full')

        if np.allclose(auto_corr, np.flip(auto_corr)):
            print("Mảng âm thanh là nhân quả.")
        else:
            print("Mảng âm thanh không phải là nhân quả.")
    def fft(self,a):
        X = fftpack.fft(a.a)
        return X
    
    def ifft(self,a):
        X = fftpack.ifft(a.a)
        return X

    def lowpass_filter(self,
                       audio, # doi tuong audio
                       cutoff, # ngưỡng cắt 
                    #    fs, # tần số lấy mẫu
                       order=5):
        nyq = 0.5 * audio.sr
        normal_cutoff = cutoff / nyq
        b, a = signal.butter(order, normal_cutoff, btype='low', analog=False)
        y = signal.lfilter(b, a, audio.a)
        return y
    
    def highpass_filter(self,
                        audio, 
                        cutoff, # ngưỡng cắt 
                        # fs, # ngưỡng cắt 
                        order=5):
        nyq = 0.5 * audio.sr
        normal_cutoff = cutoff / nyq
        b, a = signal.butter(order, normal_cutoff, btype='high', analog=False)
        y = signal.lfilter(b, a, audio.a)
        return y
    
    # Bộ lọc thông thấp cực đại (Low-pass Chebyshev filter)
    def chebyshev_lowpass_filter(self,
                                 audio, #doi tuong audio
                                 cutoff, # ngưỡng cắt 
                                #  fs, # ngưỡng cắt 
                                 rp=0.1, order=5):
        nyq = 0.5 * audio.sr
        Wn = cutoff / nyq
        b, a = signal.cheby1(order, rp, Wn, btype='low', analog=False)
        y = signal.filtfilt(b, a, audio.a)
        return y
    
    # Bộ lọc thông cao cực đại (High-pass Chebyshev filter):
    def chebyshev_highpass_filter(self, 
                                  data, 
                                  cutoff, 
                                #   fs, 
                                  rp=0.1, 
                                  order=5):
        nyq = 0.5 * data.sr
        Wn = cutoff / nyq
        b, a = signal.cheby1(order, rp, Wn, btype='high', analog=False)
        y = signal.filtfilt(b, a, data.a)
        return y
    
    # bo loc can bang
    # def linear_equalizer(self, data, gains):
    #     # Tạo bộ lọc FIR với đáp ứng tần số theo mảng gains
    #     print(data.sr)
    #     b = signal.firwin(len(gains), [0, data.sr//2], fs=data.sr, window='boxcar')

    #     # Nhân hệ số tần số của bộ lọc với mảng gains
    #     b *= gains

    #     # Áp dụng bộ lọc FIR vào tín hiệu âm thanh đầu vào
    #     y = signal.filtfilt(b, 1, data)
    #     return y
    
    def linear_equalizer(self,data, gains):
    # Tạo bộ lọc FIR với các trọng số được chỉ định bởi mảng gains
        b = gains
        # Áp dụng bộ lọc FIR vào tín hiệu âm thanh đầu vào bằng cách sử dụng hàm convolve()
        y = np.convolve(data.a, b, mode='same')
        return y
    
    # tuy chinh can bang
    def custom_equalizer(self,data, cutoffs, gains):
        num_taps = 1000 # số lượng hệ số của bộ lọc
        nyq = 0.5 * data.sr
        cutoffs = np.array(cutoffs) / nyq
        b = signal.firwin(num_taps, cutoffs, pass_zero=False, gains=gains, window='hann')
        y = signal.filtfilt(b, 1, data.a)
        return y


    

    