from concurrent import futures
import logging

import grpc

import get_value_pb2
import get_value_pb2_grpc

from common import generate_payload


class Main(get_value_pb2_grpc.MainServicer):

    def GetValue(self, request, context):
        return get_value_pb2.ValueReply(value=generate_payload(request.size))


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    get_value_pb2_grpc.add_MainServicer_to_server(Main(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
