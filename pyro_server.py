#!/usr/bin/python

from __future__ import unicode_literals, print_function, absolute_import

import Pyro.core

from common import generate_payload


class SimplePyroServer(Pyro.core.ObjBase):

    def get_value(self, size, payload):
        return generate_payload(size)


def main(port):
    Pyro.core.initServer()
    d = Pyro.core.Daemon(port=port)
    d.connect(SimplePyroServer(), 'root')
    d.requestLoop()


if __name__ == '__main__':
    main(8011)
