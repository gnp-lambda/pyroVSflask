from __future__ import unicode_literals, print_function, absolute_import

import string
import random


def generate_payload(size):
    return ''.join(random.choice(string.ascii_letters) for _ in range(size))
