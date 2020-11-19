from pyfirmata2 import Arduino
import time

board = Arduino('/dev/ttyACM3')

#Sample every 20ms
board.samplingOn(20)

board.analog[0].register_callback(myCallback)
board.analog[0].enable_reporting()