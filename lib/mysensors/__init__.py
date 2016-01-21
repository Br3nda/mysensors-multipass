import serial
import requests


def default_handler(key, value, station):
    print "Key = '{key}', value='{val}'".format(
        key=key,
        val=val)


def listen_for_data(port, speed=115200, handler=default_handler):
    ser = serial.Serial(port, speed)
    while True:
        try:
            line = ser.readline().strip()
            line = line[:-1]
            print line
            if line.startswith('R>'):
                line = line.replace('R>', '')
                station = line.split(':')[0]
                print "station = {station}".format(station=station)
                line = line.replace(station + ':', '')
                parts = line.split(';')
                for p in parts:
                    key, val = p.split('=')
                    handler(key=key, value=val, station=station)
            else:
                print "unrecognised message: ", line
        except Exception, e:
            print e
