from unittest import TestCase
from mysensors.message import Message
class MessageTests (TestCase):
	def test_startup_decoding(self):
		test_data = '0;0;3;0;9;gateway started, id=0, parent=0, distance=0'
		result = Message.decode(test_data)
	
	def test_startup_message(self):
		test_data = '0;0;3;0;14;Gateway startup complete.'
		result = Message.decode(test_data)
		self.assertEqual(result, 1)