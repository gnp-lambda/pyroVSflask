
from __future__ import unicode_literals, print_function, absolute_import

import requests

from common import generate_payload


http_session = requests.Session()


def main(size):
    payload = generate_payload(size)
    response = http_session.post('http://localhost:8000/get_value/%s' % size,
                                 data=payload, headers={'Content-Type': 'text'})
    return response.content


if __name__ == '__main__':
    print(main(100))
