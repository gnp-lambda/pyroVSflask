
from __future__ import unicode_literals, print_function, absolute_import

import os
import requests

from common import generate_payload

SERVER = os.environ.get('SERVER', 'http://localhost:8000')

http_session = requests.Session()


def main(size):
    payload = generate_payload(size)
    response = http_session.post('%s/get_value/%s' % (SERVER, size),
                                 data=payload, headers={'Content-Type': 'text'})
    return response.content


if __name__ == '__main__':
    print(main(100))
