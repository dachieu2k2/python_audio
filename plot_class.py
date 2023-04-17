import matplotlib.pyplot as plt

class BieuDo:
    def inBieuDo(audio,color):
        plt.plot(audio,color=color)
        plt.show()

    def inBieuDoTrcVaSau(audio1,color1,audio2,color2,title):
        plt.figure(num=title)

        plt.plot(audio1.a,color1)
        plt.plot(audio2,color2)
        plt.show()
        
    def inBieuDoTrcVaSau2(audio1,color1,audio2,color2,title):
        plt.figure(num=title)
        plt.subplot(2,1,1)
        plt.title('Đoạn âm thanh ban đầu')
        plt.plot(audio1.a,color1)
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
        plt.grid()

        plt.subplot(2,1,2)
        plt.title('Đoạn âm thanh lúc sau')
        plt.plot(audio2,color2)
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
        plt.tight_layout()
        plt.grid()

        plt.show()