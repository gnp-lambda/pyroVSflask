
from __future__ import unicode_literals, print_function, absolute_import

# import requests
import Pyro.core

from common import generate_payload


def get_pyro_server(uri):
    return Pyro.core.getProxyForURI(uri)


def get_pyro_value(server, size, payload_size=1024):
    payload = generate_payload(payload_size)
    return server.get_value(size, payload)


def main(size):
    server = get_pyro_server('PYROLOC://localhost:8011/root')
    return get_pyro_value(server, size, size)


if __name__ == '__main__':
    print(main(100))
