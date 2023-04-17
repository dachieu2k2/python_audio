import numpy as np

from audio_class import Audio
from tinh_toan_class import TinhToan
from plot_class import BieuDo
from loc_class import Loc
from effect_class import HieuUng




# khoi tao
Audio1 = Audio('./Sounds/1.mp3')
Audio2 = Audio('./Sounds/2.wav')

# audio thay doi kich thuoc de phu hop vs audio 2
Audio2.thayDoiKichThuoc(Audio1)

# Tinh toan
tinhToan = TinhToan()

loc = Loc()


# mode = 'LPF' | 'BDF' | 'BSF' | 'HPF' | 'EQ'
# window = 'bartlett' | 'hamming' | 'hanning' | 'blackman'
#

#
value = np.convolve(loc.loc_am_thanh('LPF','bartlett'), Audio1.a, mode='same')
BieuDo.inBieuDoTrcVaSau2(audio1=Audio1,color1='red',color2='blue',audio2=value, title="Lọc LPF với cửa sổ bartlett")

value1 = np.convolve(loc.loc_am_thanh('BDF','blackman'), Audio1.a, mode='same')
BieuDo.inBieuDoTrcVaSau2(audio1=Audio1,color1='red',color2='blue',audio2=value1, title="Lọc BDF với cửa sổ blackman")

value2 = np.convolve(loc.loc_am_thanh('BSF','blackman'), Audio1.a, mode='same')
BieuDo.inBieuDoTrcVaSau2(audio1=Audio1,color1='red',color2='blue',audio2=value2, title="Lọc BSF với cửa sổ blackman")

value3 = np.convolve(loc.loc_am_thanh('HPF','blackman'), Audio1.a, mode='same')
BieuDo.inBieuDoTrcVaSau2(audio1=Audio1,color1='red',color2='blue',audio2=value3, title="Lọc HPF với cửa sổ blackman")

value4 = np.convolve(loc.loc_am_thanh('EQ','blackman'), Audio1.a, mode='same')
BieuDo.inBieuDoTrcVaSau2(audio1=Audio1,color1='red',color2='blue',audio2=value4, title="Lọc EQ với cửa sổ blackman")


hieuUng = HieuUng()


BieuDo.inBieuDoTrcVaSau2(audio1=Audio1,color1='red',color2='blue',audio2=hieuUng.echo(Audio1), title="Echo")
BieuDo.inBieuDoTrcVaSau2(audio1=Audio1,color1='red',color2='blue',audio2=hieuUng.reversal(Audio1), title="reversal")
BieuDo.inBieuDoTrcVaSau2(audio1=Audio1,color1='red',color2='blue',audio2=hieuUng.dangle(Audio1), title="dangle")
BieuDo.inBieuDoTrcVaSau2(audio1=Audio1,color1='red',color2='blue',audio2=hieuUng.fade_in(Audio1), title="Fade In")
BieuDo.inBieuDoTrcVaSau2(audio1=Audio1,color1='red',color2='blue',audio2=hieuUng.fade_out(Audio1), title="Fade Out")
BieuDo.inBieuDoTrcVaSau2(audio1=Audio1,color1='red',color2='blue',audio2=hieuUng.modulation(Audio1), title="modulation")


        


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