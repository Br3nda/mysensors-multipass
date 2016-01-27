from mysensors import decode_message_type
class Message:
  ##
  # node-id
  # ;child-sensor-id
  # ;message-type
  # ;ack
  # ;sub-type
  # ;payload
  # \n

  def __init__(self, sentence):
    sentence = sentence.strip()

    (node_id,
      child_sensor_id,
      messsage_type,
      ack,
      sub_type,
      payload) = sentence.split(';')

    self.node_id = int(node_id)
    self.child_sensor_id = int(child_sensor_id)
    self.message_type = decode_message_type(int(messsage_type))
    self.ack = ack
    self.sub_type = sub_type
    self.payload = payload

  def decode_payload(self):
    print self.payload
    # return payload

  def __str__(self):
    return "node_id={self.node_id} child_sensor_id={self.child_sensor_id} message_type={self.message_type} ack={self.ack} sub_type={self.sub_type} payload={self.payload}".format(self=self)
