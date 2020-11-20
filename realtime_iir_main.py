from pyfirmata2 import Arduino
import scipy.signal as signal
import numpy as np
import iir_filter as iir
import matplotlib.pyplot as plt
import RealtimePlotWindow as rtpw

realtimePlotWindow = rtpw.RealtimePlotWindow()

fs = 100
fc = 2

b,a = signal.butter(2,2*fc/fs)
sos = signal.butter(4,2*fc/fs,output='sos')
filter = iir.IIR2Filter(b,a)
#filter = iir.IIR2Filter(sos)

def myCallback(data):
    realtimePlotWindow.addData(filter.filter(data))

board = Arduino('/dev/ttyACM3')

#Sample every 1000/fs milliseconds
board.samplingOn(1000/fs)

board.analog[0].register_callback(myCallback)
board.analog[0].enable_reporting()


plt.show()

# needs to be called to close the serial port
board.exit()