import serial
import requests

# The pattern is:
# node-id;child-sensor-id;message-type;ack;sub-type;payload\n


def default_handler(node_id, sub_type, payload):
    print "Key = '{node_id} {sub_type}', payload='{payload}'".format(
        node_id=node_id,
        sub_type=sub_type,
        payload=payload)


def listen_for_data(port, speed=115200, handler=default_handler):
    print "listening"
    ser = serial.Serial(port, speed)
    while True:
        try:
            line = ser.readline().strip()
            print line
            # node-id;child-sensor-id;message-type;ack;sub-type;payload\n
            (node_id,
                child_sensor_id,
                messsage_type,
                ack,
                sub_type,
                payload) = line.split(';')

            if messsage_type == M_SET:
                handler(node_id=node_id, sub_type=sub_type, payload=payload)
        except Exception, e:
            print e
