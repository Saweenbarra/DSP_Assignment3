from pyfirmata2 import Arduino
import scipy.signal as signal
import numpy as np
import iir_filter as iir
import matplotlib.pyplot as plt
import RealtimePlotWindow as rtpw
import time
import threading

unfilteredPlot = rtpw.RealtimePlotWindow()
filteredPlot = rtpw.RealtimePlotWindow()

sampleCount = 0
timer_run = 1

def timerfunc():
    global sampleCount
    global timer_run
    while(timer_run):
        time.sleep(10)
        print(sampleCount)
        sampleCount = 0

timer = threading.Thread(target=timerfunc)

fs = 100
fc = 1

#b,a = signal.cheby1(6,0.5,2*fc/fs)
#sos = signal.cheby1(6,0.5,2*fc/fs,output='sos')
b,a = signal.butter(6,2*fc/fs)
sos = signal.butter(6,2*fc/fs,output='sos')
w,h = signal.freqz(b,a)
plt.figure(3)
plt.plot(w/np.pi/2,20*np.log10(np.abs(h)))
#filter = iir.IIR2Filter(b,a)
filter = iir.IIRFilter(sos)

def myCallback(data):
    unfilteredPlot.addData(data)
    filteredPlot.addData(filter.filter(data))
    global sampleCount
    sampleCount += 1


board = Arduino('/dev/ttyACM3')

#Sample every 1000/fs milliseconds
board.samplingOn(1000/fs)

board.analog[0].register_callback(myCallback)
board.analog[0].enable_reporting()
timer.start()


plt.show()
timer_run = 0
# needs to be called to close the serial port
board.exit()