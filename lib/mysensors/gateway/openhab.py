class Config:
    URL = None
    URL_PATTERN = 'http://{url}/rest/items/Arduino_{node_id}{sub_type}/state'
    HTTP_HEADERS = {'Content-Type': 'text/plain'}


def configure_for_openhab(url=''):
    configuration.url = url


def send_status_to_openhab(node_id, sub_type, payload):
    url = Config.URL_PATTERN.format(url=Config.URL,
                                    node_id=node_id,
                                    sub_type=sub_type)

    print url
    print payload
    response = requests.put(url,
                            headers=Config.HTTP_HEADERS,
                            data=str(payload))
    print response.text

    if response.status_code != requests.codes.ok:
        response.raise_for_status()
