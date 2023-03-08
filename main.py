# 傅立葉轉換目的:了解原始訊號是由哪些頻率的cos,sin組成
# 每個signal都是sin, cos以不同頻率組成，因此FT轉換目的是要得知signal由哪些頻率的sin, cos組成
# FT轉換後，大致上會得到實部 (cos) 跟虛部 (sin)，因此做圖因該分為實部與虛部來畫
# 如果signal裡面只含有cos訊號，則得到的FT頻域應當只含有實部，這也是在積分項evev(cos)*odd(sin)會為0的原因


import numpy as np
import matplotlib.pyplot as plt
from cmath import sqrt
import seaborn as sns; sns.set()

def dft(x_sig, n = 0, X_sig = []):
    X_sig.append(dt*sum([x_sig[k] * np.exp(-2*pi*sqrt(-1)*n*k/N) for k in range(N)]))

    if n >= N-1:
        return X_sig
    return dft(x_sig, n+1, X_sig)

def idft(X_sig, k = 0, x_sig = []):
    x_sig.append(1/(N*dt)*sum([X_sig[n] * np.exp(2*pi*sqrt(-1)*n*k/N) for n in range(N)]))

    if k >= N-1:
        return x_sig
    return idft(X_sig, k+1, x_sig)

def frequency_shift():
    fs = 1/dt
    fN = fs/2
    df = 1/T
    f = np.append(np.arange(0, fN, df), np.arange(-fN, 0, df))
    return f.round(5)

def delta_function(f, f_impulse):
    output = [0]*len(f)
    for i, v in enumerate(f):
        if v == f_impulse:
            output[i] = 1
    return output

if __name__ == "__main__":
    N = 128
    T = 12
    dt = T/N
    pi = 3.1416
    k = [v for v in range(N)]
    times = [kk*dt for kk in k]
    f = frequency_shift()

    x_sig = [3*np.cos(0.5*pi*kk*dt) + 5*np.sin(2*pi*kk*dt) for kk in k]
    X_sig = dft(x_sig)

    fig = plt.figure(figsize=(10,8))

    ax1 = fig.add_subplot(221)
    # ax1.plot([n*T/256 for n in range(256)], [3*np.cos(0.5*pi*kk*T/256) + 5*np.sin(2*pi*kk*T/256) for kk in range(256)], label="Continuos")
    ax1.plot(times, x_sig, label="Continuos")
    ax1.scatter(times, x_sig, label="Discrete", color='r', alpha=0.5)
    ax1.legend(loc="upper right")
    ax1.set(xlabel="Time(sec)", ylabel="h(t)", title="Original-Continous")

    ax2 = fig.add_subplot(222)
    ax2.stem(f, [1/T*X.real for X in X_sig], basefmt=" ", label="DFT-Real", markerfmt="o") # after dft, the y-scale need to change by * 1/T
    ax2.stem(f, [1/T*X.imag for X in X_sig], basefmt=" ", linefmt="r--", markerfmt="ro", label="DFT-Image")
    ax2.legend(loc="upper right")
    ax2.set(xlabel="Frequency", ylabel="H(f)", title="DFT")

    # IDFT
    X_sig_real = np.array([1.5*v for v in delta_function(f, 0.25)]) + np.array([1.5*v for v in delta_function(f, -0.25)])
    X_sig_imag = np.array([-2.5*v for v in delta_function(f, -1)]) - np.array([-2.5*v for v in delta_function(f, 1)])

    ax3 = fig.add_subplot(223)
    ax3.stem(f, X_sig_real, label="H(f)-Real", basefmt=" ", markerfmt="o")
    ax3.stem(f, -X_sig_imag, label="H(f)-Image", basefmt=" ", linefmt="r--", markerfmt="ro")
    ax3.legend(loc="upper right")
    ax3.set(xlabel="Frequency", ylabel="H(f)", title="Original-Continous")

    x_sig_inverse = idft(X_sig_real - sqrt(-1)*X_sig_imag)

    ax4 = fig.add_subplot(224)
    ax4.scatter(times, T*np.array(x_sig_inverse), color='r', alpha=0.5, label="Discrete") # after idft, the y-scale need to change by * T
    ax4.plot(times, T*np.array(x_sig_inverse), label="h(t)")
    ax4.legend(loc="upper right")
    ax4.set(xlabel="Time(sec)", ylabel="h(t)", title="IDFT")
    fig.tight_layout() # avoid overlap
    plt.show()
