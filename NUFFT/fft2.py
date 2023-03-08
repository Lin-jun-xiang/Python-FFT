import pandas as pd                 # 匯入Pandas庫，用於資料處理
import numpy as np                  # 匯入Numpy庫，用於數值計算、使用傅立葉轉換模組
from scipy.interpolate import interp1d   # 匯入SciPy庫中的插值函數，用於資料插值
import matplotlib.pyplot as plt     # 匯入Matplotlib庫，用於繪圖
import seaborn as sns; sns.set()    # 匯入Seaborn庫，用於美化繪圖風格

def generate_interval_data(N: int):
    """
    用於生成一個新的等間隔採樣的時間序列，以及對應的數據
    N: 新的樣本數量
    """
    interp_time = np.linspace(time.min(), time.max(), num=N)     # 等間隔採樣時間序列
    interp_data = interp1d(time, data, kind='linear')(interp_time)   # 插值生成新的數據

    return interp_time, interp_data

def fft():
    """
    用於將數據進行傅立葉轉換、並計算相對應頻率序列
    """
    dft = np.fft.fft(interp_data)       # 對插值後的數據進行FFT分析

    freq = np.fft.fftfreq(len(interp_data), interp_time[1] - interp_time[0])   # 計算對應的頻率序列

    return dft, freq

def plot_():
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))    # 創建一個包含兩個子圖的Figure對象 (垂直)

    # 時域圖
    ax1.plot(time, df["NDVI_grass_mean"], color="black")    # 繪製原始時序圖
    ax1.scatter(time, df["NDVI_grass_mean"], label="sample", color='r', alpha=0.7)   # 將原始數據點繪製在時序圖上
    ax1.legend(loc="upper right")   # 添加圖例
    ax1.set(xlabel="Time(day)", ylabel="NDVI_grass_mean")   # 設置X軸和Y軸的標籤
    ax1.set_title("NVDI time series", color="red")   # 設置標題

    # 實部頻譜
    real_dft = abs(dft)    # 計算DFT的實部
    ax2.plot(freq, real_dft, color="royalblue")   # 繪製頻譜圖
    ax2.scatter(freq, real_dft, color='royalblue', linewidth=1)   # 將頻譜數據點繪製在頻譜圖上
    ax2.set(xlabel=f"Cycles per {time.max()} days", ylabel="NDFT")   # 設置X軸和Y軸的標籤
    ax2.set_title("FFT", color="red") # 設置標題
    ax2.set_xlim([-5, freq.max()+5]) # 設置 x 軸範圍

    fig.subplots_adjust(hspace=0.5) # 設置兩個子圖的間距

    plt.show()

if __name__ == "__main__":
    df = pd.read_excel("./fft.xlsx") # 讀取 excel 檔案

    time = df["days_first"] # 取出時間資料
    data = df["NDVI_grass_mean"] # 取出 grass mean
    data = data - data.mean() # 去中心化

    N = 160 # 定義總採樣點數量 (原始採樣量為80，透過內插方式變成160)
    interp_time, interp_data = generate_interval_data(N) # 呼叫自定義內插函式，得到新的等間距數據組

    dft, freq = fft() # 呼叫自定義快速傅立葉轉換函式
    freq = freq * time.max() # 將 x 軸乘上 2852 days
    freq = freq[:N//2] # 取出右半邊正頻部分
    dft = dft[:N//2] # 取出右半邊正頻部分
    plot_() # 呼叫自定義繪圖函式