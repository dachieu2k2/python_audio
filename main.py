from audio_class import Audio
from tinh_toan_class import TinhToan
from plot_class import BieuDo
import numpy as np



# khoi tao
Audio1 = Audio('./Sounds/1.mp3')
Audio2 = Audio('./Sounds/2.wav')

# audio thay doi kich thuoc de phu hop vs audio 2
Audio2.thayDoiKichThuoc(Audio1)

# Tinh toan
tinhToan = TinhToan()
# value = tinhToan.TichHaiVector(Audio2,Audio1)
# value1 = tinhToan.TongHaiVector(Audio2,Audio1)
# value2 = tinhToan.ThuongHaiVector(Audio2,Audio1)
# value3 = tinhToan.HieuHaiVector(Audio2,Audio1)
# value4 = tinhToan.NhanChapVector(Audio2,Audio1)
# value5 = tinhToan.NhanTuongQuan(Audio2,Audio1)
# value6 = tinhToan.DichThoiGian(a=Audio1,s=-10)
# value7 = tinhToan.DaoThoiGian(a=Audio1)
# value8 = tinhToan.CongSuatNangLuong(Audio1)
# # value9 = tinhToan.dft(a=Audio1)
# value9 = tinhToan.fft(Audio1)
# value10 = tinhToan.fft(Audio1)
# print(value9)
# tinhToan.KiemTraNhanQua(Audio1,Audio2)

        
# BieuDo.inBieuDoTrcVaSau2(audio1=Audio1,color1='red',color2='blue',audio2=value, title="Tích hai tín hiệu")
# BieuDo.inBieuDoTrcVaSau2(audio1=Audio1,color1='red',color2='blue',audio2=value1, title="Tổng hai tín hiệu")
# BieuDo.inBieuDoTrcVaSau2(audio1=Audio1,color1='red',color2='blue',audio2=value2, title="Thương hai tín hiệu")
# BieuDo.inBieuDoTrcVaSau2(audio1=Audio1,color1='red',color2='blue',audio2=value3, title="Hiệu hai tín hiệu")
# BieuDo.inBieuDoTrcVaSau2(audio1=Audio1,color1='red',color2='blue',audio2=value4, title="Nhân chập hai tín hiệu")
# BieuDo.inBieuDoTrcVaSau2(audio1=Audio1,color1='red',color2='blue',audio2=value5, title="Nhân tương quan hai tín hiệu")
# BieuDo.inBieuDoTrcVaSau(audio1=Audio1,color1='red',color2='blue',audio2=value6, title="Dịch thời gian tín hiệu")
# BieuDo.inBieuDoTrcVaSau2(audio1=Audio1,color1='red',color2='blue',audio2=value7, title="Đảo thời gian tín hiệu")
# BieuDo.inBieuDoTrcVaSau2(audio1=Audio1,color1='red',color2='blue',audio2=value9, title="FFT")
# BieuDo.inBieuDoTrcVaSau2(audio1=Audio1,color1='red',color2='blue',audio2=value10, title="IFFT")



print(Audio1.sr)
value11 = tinhToan.lowpass_filter(Audio1,100)
value12 = tinhToan.highpass_filter(Audio1,100)
value13 = tinhToan.chebyshev_lowpass_filter(Audio1,100)
value14 = tinhToan.chebyshev_highpass_filter(Audio1,100)

# Tạo mảng gains
gains = np.ones(Audio1.sr//2)
gains[5000] = 2
gains[10000] = 0.5

value15 = tinhToan.linear_equalizer(Audio1,gains)
# BieuDo.inBieuDoTrcVaSau2(audio1=Audio1,color1='red',color2='blue',audio2=value11, title="LF")
# BieuDo.inBieuDoTrcVaSau2(audio1=Audio1,color1='red',color2='blue',audio2=value12, title="LF")
# BieuDo.inBieuDoTrcVaSau2(audio1=Audio1,color1='red',color2='blue',audio2=value13, title="LF")
# BieuDo.inBieuDoTrcVaSau2(audio1=Audio1,color1='red',color2='blue',audio2=value14, title="LF")
BieuDo.inBieuDoTrcVaSau2(audio1=Audio1,color1='red',color2='blue',audio2=value15, title="CAn bang")



        
