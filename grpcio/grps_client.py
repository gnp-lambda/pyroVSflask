from __future__ import unicode_literals, print_function, absolute_import

import logging
import os

import grpc

import get_value_pb2
import get_value_pb2_grpc

from common import generate_payload

SERVER = os.environ.get('SERVER', 'localhost:50051')

def main(size):
    with grpc.insecure_channel(SERVER) as channel:
        stub = get_value_pb2_grpc.MainStub(channel)
        response = stub.GetValue(get_value_pb2.ValueRequest(value=generate_payload(size), size=size))
    return response.value


if __name__ == '__main__':
    print(main(100))
