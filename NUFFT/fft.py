import pandas as pd
import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

def generate_interval_data(N: int):
    """
    N: new number of samples
    """
    interp_time = np.linspace(time.min(), time.max(), num=N)
    interp_data = interp1d(time, data, kind='linear')(interp_time)

    return interp_time, interp_data

def fft():
    dft = np.fft.fft(interp_data)

    freq = np.fft.fftfreq(len(interp_data), interp_time[1] - interp_time[0])

    return dft, freq

def plot_():
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

    # 時域圖
    ax1.plot(time, df["NDVI_grass_mean"], color="black")
    ax1.scatter(time, df["NDVI_grass_mean"], label="sample", color='r', alpha=0.7)
    ax1.legend(loc="upper right")
    ax1.set(xlabel="Time(day)", ylabel="NDVI_grass_mean")
    ax1.set_title("NVDI time series", color="red")

    # 實部頻譜
    real_dft = abs(dft)
    ax2.plot(freq, real_dft, color="royalblue")
    ax2.scatter(freq, real_dft, color='royalblue', linewidth=1)
    ax2.set(xlabel=f"Cycles per {time.max()} days", ylabel="NDFT")
    ax2.set_title("FFT", color="red")
    ax2.set_xlim([-5, freq.max()+5])

    fig.subplots_adjust(hspace=0.5)

    plt.show()

if __name__ == "__main__":
    df = pd.read_excel("./fft.xlsx")

    time = df["days_first"]
    data = df["NDVI_grass_mean"]
    data = data - data.mean()

    N = 160
    interp_time, interp_data = generate_interval_data(N)

    dft, freq = fft()
    freq = freq * time.max()
    freq = freq[:N//2]
    dft = dft[:N//2]
    plot_()
