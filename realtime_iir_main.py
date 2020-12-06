from pyfirmata2 import Arduino
import scipy.signal as signal
import numpy as np
import iir_filter as iir
import matplotlib.pyplot as plt
import RealtimePlotWindow as rtpw
import time
import threading

#Plotting windows
unfilteredPlot = rtpw.RealtimePlotWindow()
filteredPlot = rtpw.RealtimePlotWindow()

#Non-blocking timer thread variables
sampleCount = 0
timer_run = 1

#Non-blocking timer thread
def timerfunc():
    global sampleCount
    global timer_run
    while(timer_run):
        time.sleep(10)
        print(sampleCount)
        sampleCount = 0

timer = threading.Thread(target=timerfunc)

fs = 100 #Sampling at 100Hz
fc = 1 #1Hz cut-off frequency

#Generate sos coefficients
sos = signal.butter(6,2*fc/fs,output='sos')

#Create the filter object
filter = iir.IIRFilter(sos)

#Callback function triggered by Arduino
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

#Start timer to check data acquisition rate
timer.start()

plt.show()

#Kill the timer thread
timer_run = 0

board.exit()