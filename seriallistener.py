from mysensors.gateway.openhab import configure_for_openhab, send_status_to_openhab
from mysensors.listener import listen_for_data

# configure_for_openhab(url="http://127.0.0.1:8080")
listen_for_data(port='/dev/ttyUSB0') #, handler=send_status_to_openhab)
