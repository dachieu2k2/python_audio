import numpy as np
import matplotlib.pyplot as plt

class Loc:
    def __init__(self, N=101, fc=1000, fl=500, fh=1500, f1=2000,f2=3000,fs=44100,bw=100):
        # Kích thước mẫu lọc
        self.N = N

        # Tần số cắt của bộ lọc LPF
        self.fc = fc

        # Tần số cắt thấp của bộ lọc BPF
        self.fl = fl

        # Tần số cắt cao của bộ lọc BPF
        self.fh = fh

        # Tần số cắt của bộ lọc BSF
        self.f1 = f1
        self.f2 = f2

        # Tần số lấy mẫu
        self.fs = fs

        # Tần số tối đa
        self.ft = fs / 2

        # Độ rộng băng thông của bộ lọc EQ
        self.bw = bw

    # Hàm đáp ứng xung lý tưởng của bộ lọc LPF
    def ideal_filter_response_LPF(self, n, fc, ft):
        if n == (ft - fc):
            return 2 * fc / ft
        elif n == (ft + fc):
            return 2 * (1 - fc / ft)
        else:
            return np.sin(2 * np.pi * fc * (n - (ft - 1) / 2)) / (np.pi * (n - (ft - 1) / 2))

    # Hàm đáp ứng xung lý tưởng của bộ lọc BPF
    def ideal_filter_response_BPF(self, n, fl, fh, ft):
        if n == (ft - fh):
            return 2 * fh / ft
        elif n == (ft + fh):
            return 2 * (1 - fh / ft)
        elif n == (ft - fl):
            return 2 * fl / ft
        elif n == (ft + fl):
            return 2 * (1 - fl / ft)
        else:
            return (np.sin(2 * np.pi * fh * (n - (ft - 1) / 2)) / (np.pi * (n - (ft - 1) / 2))) - (np.sin(2 * np.pi * fl * (n - (ft - 1) / 2)) / (np.pi * (n - (ft - 1) / 2)))

    # Hàm đáp ứng xung lý tưởng của bộ lọc BSF
    def ideal_filter_response_BSF(self, n, f1, f2, ft):
        if n == 0:
            return 2*(f2-f1)/ft
        else:
            return (np.sin(2*np.pi*f1*(n-(ft-1)/2))/(np.pi*(n-(ft-1)/2))) - (np.sin(2*np.pi*f2*(n-(ft-1)/2))/(np.pi*(n-(ft-1)/2)))

    # Hàm đáp ứng xung lý tưởng của bộ lọc HPF
    def ideal_filter_response_HPF(self, n, fc, ft):
        if n == (ft - fc):
            return 2 * (1 - fc / ft)
        elif n == (ft + fc):
            return 2 * fc / ft
        else:
            return -np.sin(2 * np.pi * fc * (n - (ft - 1) / 2)) / (np.pi * (n - (ft - 1) / 2))
        
    # Hàm đáp ứng xung lý tưởng của bộ lọc EQ
    def ideal_filter_response_EQ(self, n, fc, bw, ft):
        if (n == (ft - fc - bw/2)):
            return 0.5
        elif (n == (ft - fc + bw/2)):
            return 0.5
        elif (n > (ft - fc - bw/2)) and (n < (ft - fc + bw/2)):
            return 1.0
        else:
            return 0.0

    
    # Tạo ra hàm đáp ứng xung lý tưởng h(n) của bộ lọc LPF
    def arr_LPF(self):
        h_lpf = np.zeros(self.N)
        for n in range(self.N):
            h_lpf[n] = self.ideal_filter_response_LPF(n, self.fc, self.ft)
        
        return h_lpf


    # Tạo ra hàm đáp ứng xung lý tưởng h(n) của bộ lọc BPF
    def arr_BDF(self):
        h_bpf = np.zeros(self.N)
        for n in range(self.N):
            h_bpf[n] = self.ideal_filter_response_BPF(n, self.fl, self.fh, self.ft)

        return h_bpf

    # Tạo ra hàm đáp ứng xung lý tưởng h(n) của bộ lọc BSF
    def arr_BSF(self):
        h_bsf = np.zeros(self.N)
        for n in range(self.N):
            h_bsf[n] = self.ideal_filter_response_BSF(n, self.f1, self.f2, self.ft)

        return h_bsf

    # Tạo ra hàm đáp ứng xung lý tưởng h(n) của bộ lọc HPF
    def arr_HPF(self):
        h_hpf = np.zeros(self.N)
        for n in range(self.N):
            h_hpf[n] = self.ideal_filter_response_HPF(n, self.fc, self.ft)

        return h_hpf

    # Tạo ra hàm đáp ứng xung lý tưởng h(n) của bộ lọc EQ
    def arr_EQ(self):
        h_eq = np.zeros(self.N)
        for n in range(self.N):
            h_eq[n] = self.ideal_filter_response_EQ(n, self.fc, self.bw, self.ft)
        return h_eq

    def loc_am_thanh(self, mode, window):

        # tao mang theo mode
        arr_loc = self.arr_LPF()
        if mode == 'LPF':
            arr_loc = self.arr_LPF()
        elif mode == 'BDF':
            arr_loc = self.arr_BDF()
        elif mode == 'BSF':
            arr_loc = self.arr_BSF()
        elif mode == 'HPF':
            arr_loc = self.arr_HPF()
        elif mode == 'EQ':
            arr_loc = self.arr_EQ()
        else:
            arr_loc = self.arr_LPF()

        # tao cua so theo mode
        window_loc = np.hanning(self.N)
        if window == 'bartlett':
            window_loc = np.bartlett(self.N)
        elif window == 'hamming':
            window_loc = np.hamming(self.N)
        elif window == 'hanning':
            window_loc = np.hanning(self.N)
        else:
            window_loc = np.blackman(self.N)

        # Nhân hàm cửa sổ vào hàm đáp ứng xung lý tưởng của bộ lọc 
        # print(window_loc)
        # print (arr_loc * window_loc)
        return arr_loc * window_loc






