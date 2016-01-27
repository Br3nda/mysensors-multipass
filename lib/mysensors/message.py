class Message:
  ##
  # node-id
  # ;child-sensor-id
  # ;message-type
  # ;ack
  # ;sub-type
  # ;payload
  # \n
  @classmethod
  def decode(cls, sentence):
    message = Message(node_id, child_sensor_id, message_type, ack, sub_type, payload)

  def __init__(self, node_id, child_sensor_id, message_type, ack, sub_type, payload):
    pass