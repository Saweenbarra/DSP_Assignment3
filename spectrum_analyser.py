import numpy as np
import scipy.io.wavfile as wavfile
import matplotlib.pyplot as plt

#Load wav file sample frequency and data
data = np.loadtxt("data.dat")
fs = 100
#Calculate duration of sample and create time (x-axis) array
duration = len(data)/fs
t = np.linspace(0, duration, len(data))

#Normalising factor
normaliser = (pow(2,15)-1)

#Plot sample in time domain
plt.figure(1)
tplot = plt.plot(t, data/normaliser)
tplot = plt.xlabel("Time (s)")
tplot = plt.ylabel("Amplitude")

#Calculate the fast fourier transform of data
dataf = np.fft.fft(data)
#Convert FFT data to decibels relative to full scale (dBFS)
datafdB = 20*np.log10(abs(dataf)*2/len(dataf)/(pow(2,15)-1))

#Create frequency axis
f = np.linspace(0, fs, len(dataf))

#Plot sample in frequency domain
plt.figure(2)
fplot = plt.plot(f, datafdB)
fplot = plt.xlabel("Frequency (Hz)")
fplot = plt.ylabel("dBFS")
plt.xscale("log")
plt.xlim(right = fs/2) #Don't plot data after nyquist because it doesn't exist

#Find sample numbers corresponding to 85Hz and 180Hz
k1 = int(len(dataf)/fs*85)
k2 = int(len(dataf)/fs*180)

#Amplify selected frequencies by factor
dataf[k1:k2+1] *= 1.2
dataf[-k2-1:-k1] *= 1.2

#Find sample numbers corresponding to 6kHz and 10kHz
k1 = int(len(dataf)/fs*6000)
k2 = int(len(dataf)/fs*10000)

#Amplify selected frequencies by factor
dataf[k1:k2+1] *= 3
dataf[-k2-1:-k1] *= 3

#Convert boosted signal to time domain
dataBoost = np.fft.ifft(dataf)
dataBoost = np.real(dataBoost)

#Cast 64bit floats to int to be written to wav file
dataBoost = dataBoost.astype(np.int16)

#Write boosted signal to wav file

plt.show() #Plot all graphs