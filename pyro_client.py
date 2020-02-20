
from __future__ import unicode_literals, print_function, absolute_import

import os
import Pyro.core

from common import generate_payload

SERVER = os.environ.get('SERVER', 'PYROLOC://localhost:8011/root')


def get_pyro_server(uri):
    return Pyro.core.getProxyForURI(uri)


def get_pyro_value(server, size, payload_size=1024):
    payload = generate_payload(payload_size)
    return server.get_value(size, payload)


def main(size):
    server = get_pyro_server(SERVER)
    return get_pyro_value(server, size, size)


if __name__ == '__main__':
    print(main(100))
