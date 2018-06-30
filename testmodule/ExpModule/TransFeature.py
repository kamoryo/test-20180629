import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class transfeature:

    def stft(self,data,rate,winwide,mov,time):
        dnum = rate*winwide
        sample = rate*time
        split = int(sample-dnum)/mov+1

        if split % 1 != 0:
            print(split)

        data_split = np.zeros((int(split),dnum))

        for i in range():
            data_split[i] = data[mov*i:dnum+mov*i]
        data_fft = sf.fft(data_split*np.hamming(dnum))/(rate/2)
        data_fs = np.sqrt(data_fft.real ** 2 + data_fft.imag ** 2)
        data_result = data_fs[:,int(dnum/2)]

        return data_result


if __name__ == "__main__":

    x = np.arange(0,10,0.05)
    y = np.sin(10*2*np.pi*x)

    plt.plot(x,y)
    plt.show()