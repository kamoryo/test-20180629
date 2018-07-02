import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.fftpack as sf

class TransFeature:
    rate = 200
    winwide = 2
    mov = 1

    def __init__(self, wave, t):
        self.data = wave
        self.time = t

    def stft(self):
        dnum = self.rate*self.winwide
        sample = self.rate*self.time
        split = sample-dnum/self.mov+1

        if split % 1 != 0:
            print(split)

        data_split = np.zeros((int(split), dnum))

        for i in range(int(split)):
            data_split[i] = self.data[self.mov*i:dnum+self.mov*i]
        data_fft = sf.fft(data_split*np.hamming(dnum))/(self.rate/2)
        data_fs = np.sqrt(data_fft.real ** 2 + data_fft.imag ** 2)
        data_result = data_fs[:, :int(dnum/2)]

        return data_result


if __name__ == "__main__":

    x = np.arange(0, 20, 0.005)
    y = np.sin(20*2*np.pi*x)

    tf = TransFeature(y, 20)
    y2 = tf.stft()

    plt.plot(y2.T)
    plt.xticks(np.arange(0,200,20),np.arange(0,100,10))
    plt.show()