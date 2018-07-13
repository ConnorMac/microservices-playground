# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc
from concurrent import futures

import transaction_pb2 as transaction__pb2


class TransactionsStub(object):
    """Interface exported by the server.
    """

    def __init__(self, channel):
        """Constructor.
        Args:
        channel: A grpc.Channel.
        """
        self.GetTransaction = channel.unary_unary(
            '/transactions.Transactions/GetTransaction',
            request_serializer=transaction__pb2.Id.SerializeToString,
            response_deserializer=transaction__pb2.Transaction.FromString,
            )
        self.ListTransactions = channel.unary_stream(
            '/transactions.Transactions/ListTransactions',
            request_serializer=transaction__pb2.Transaction.SerializeToString,
            response_deserializer=transaction__pb2.Transaction.FromString,
            )
        self.CreateTransaction = channel.unary_unary(
            '/transactions.Transactions/CreateTransaction',
            request_serializer=transaction__pb2.Transaction.SerializeToString,
            response_deserializer=transaction__pb2.Transaction.FromString,
            )


class TransactionServicer(object):
    """Interface exported by the server.
    """

    def ListTransactions(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListTransactions(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListTransactions(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TransactionServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'GetTransaction': grpc.unary_unary_rpc_method_handler(
            servicer.GetTransaction,
            request_deserializer=transaction__pb2.Id.FromString,
            response_serializer=transaction__pb2.Transaction.SerializeToString,
        ),
        'ListTransactions': grpc.unary_stream_rpc_method_handler(
            servicer.ListTransactions,
            request_deserializer=transaction__pb2.Transaction.FromString,
            response_serializer=transaction__pb2.Transaction.SerializeToString,
        ),
        'CreateTransaction': grpc.unary_unary_rpc_method_handler(
            servicer.CreateTransaction,
            request_deserializer=transaction__pb2.Transaction.FromString,
            response_serializer=transaction__pb2.Transaction.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'transactions.Transactions', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
