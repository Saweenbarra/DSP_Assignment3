from pyfirmata2 import Arduino
import time

sampleCount = 0

fs = 100

def myCallback(data):
    global sampleCount
    sampleCount += 1

board = Arduino('/dev/ttyACM3')

#Sample every 1000/fs milliseconds
board.samplingOn(1000/fs)

board.analog[0].register_callback(myCallback)
board.analog[0].enable_reporting()

time.sleep(10)

print(sampleCount)

board.exit()