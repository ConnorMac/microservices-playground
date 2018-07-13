from concurrent import futures
import time
import math

import grpc

import transaction_pb2
import transaction_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class TransactionServicer(transaction_pb2_grpc.TransactionServicer):
    """Provides methods that implement functionality of route guide server."""

    def __init__(self):
        self.transactions = {
            '1': transaction_pb2.Transaction(
                id="uuid_1",
                amount=10
            )
        }

    def GetTransaction(self, request, context):
        return self.transactions.get(request.id)

    def ListTransactions(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateTransaction(self, request, context):
        self.transactions[request.id] = request
        return request


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    transaction_pb2_grpc.add_TransactionServicer_to_server(
        TransactionServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
