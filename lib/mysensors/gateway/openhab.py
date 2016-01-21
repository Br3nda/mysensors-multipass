class configuration:
    url = None


def configure_for_openhab(url=''):
    configuration.url = url


def send_status_to_openhab(key, value, station):
    url = 'http://{host}:{port}/rest/items/Arduino_{station}{key}/state'.format(
        host=openhab_host,
        port=openhab_port,
        station=station,
        key=key)

    print url
    print value
    response = requests.put(url, headers={'Content-Type': 'text/plain'},
                            data=str(value))
    print response.text

    if response.status_code != requests.codes.ok:
        response.raise_for_status()
