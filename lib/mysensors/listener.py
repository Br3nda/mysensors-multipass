import serial
import requests
from mysensors.message import Message
# The pattern is:
# node-id;child-sensor-id;message-type;ack;sub-type;payload\n


def default_handler(message):
    print message


def listen_for_data(port, speed=115200, handler=default_handler):
    print "listening"
    ser = serial.Serial(port, speed)
    while True:
        # try:
        line = ser.readline()
        print line
        message = Message(line)
        handler(message)
        # except Exception, e:
            # print e
