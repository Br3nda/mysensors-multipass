from unittest import TestCase
from mysensors.message import Message

  ##
  # node-id
  # ;child-sensor-id
  # ;message-type
  # ;ack
  # ;sub-type
  # ;payload
  # \n
  
class PayloadTests (TestCase):
  def test_startup_decoding(self):
    m = Message('0;0;3;0;9;gateway started, id=0, parent=0, distance=0')
    self.assertEqual(m.payload, "gateway started, id=0, parent=0, distance=0")
    payload = m.decode_payload()
  
  def test_payload_decode(self):
    m = Message("0;0;3;0;9;read: 255-255-255 s=255,c=3,t=7,pt=0,l=0,sg=0:")
    self.assertEqual(m.payload, "read: 255-255-255 s=255,c=3,t=7,pt=0,l=0,sg=0:")
    payload = m.decode_payload()
    print payload
    self.assertEqual(payload['s'], "255")

  # def test_message_decode_1(self):
  #   result = Message("0;0;3;0;9;send: 0-0-255-255 s=255,c=3,t=8,pt=1,l=1,sg=0,st=bc:0")
  #   result = Message("0;0;3;0;9;read: 255-255-0 s=255,c=3,t=3,pt=0,l=0,sg=0:")
  #   result = Message("255;255;3;0;3;")

