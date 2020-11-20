from pyfirmata2 import Arduino
import scipy.signal as signal
import numpy as np

fs = 100
fc = 3

b,a = signal.butter(4,2*fc/fs)
sos = signal.butter(4,2*fc/fs,output='sos')
print(a)

board = Arduino('/dev/ttyACM3')

#Sample every 1000/fs milliseconds
board.samplingOn(1000/fs)

#board.analog[0].register_callback(myCallback)
#board.analog[0].enable_reporting()