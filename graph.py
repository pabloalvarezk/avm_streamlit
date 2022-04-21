import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import fft, fftfreq

def graph_temp(value):
   
    samplerate=8000
    a = 0
    b = len(value[:,0])
    dt = 1 / samplerate
    ta = a * dt
    tb = b * dt
    tab = np.arange(ta, tb, dt)

    fig, ax = plt.subplots()
    ax.plot(tab, value[:,0],tab,value[:,1])
    ax.set(
        xlabel="Tiempo [s]",
        ylabel="Amplitud",
    )
    ax.grid()
    ax.legend(["Microphone","Accelerometer"])
    fig.set_size_inches(20, 6)
    return fig

def graf_gvv(gvv):  
        
    samplerate=8000
    a = 0
    b = len(gvv)
    dt = 1 / samplerate
    ta = a * dt
    tb = b * dt
    tab = np.arange(ta, tb, dt)

    fig, ax = plt.subplots()
    ax.plot(tab, gvv)
    ax.set(
        xlabel="Tiempo [s]",
        ylabel="Amplitud",
    )
    ax.grid()
    ax.legend(["GVV"])
    fig.set_size_inches(20, 6)
    return fig

def graf_fft(parte): 
    # Number of samples in normalized_tone
    
    
    N   = len(parte)
    T = 1/8000
    yf = fft(parte)
    xf = fftfreq(N, T)[:N//2]

    fig, ax = plt.subplots()

    ax.plot(xf, 2.0/N * np.abs(yf)[0:N//2])
    ax.set(
            xlabel="Frecuencia [Hz]",
            ylabel="Amplitud",
        )
    ax.grid()
    ax.legend(["FFT"])
    fig.set_size_inches(20, 6)
    return fig