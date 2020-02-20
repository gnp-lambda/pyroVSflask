# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import, print_function

import timeit

REPEAT = 3
NUMBER = 1000

ClientManager = None
extraArgs = extraArgs # noqa


if __name__ == '__main__':
    timers = timeit.repeat(stmt='ClientManager.findByPrimaryKey(%s)' % extraArgs[0],
                           setup='from colofon.client.model.managers import ClientManager',
                           repeat=REPEAT, number=NUMBER)
    print("%s loops, best of 3: %s sec per loop" % (NUMBER, min(timers)))
