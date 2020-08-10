# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import american_banks_pb2 as american__banks__pb2


class AmericanBanksStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.table = channel.unary_unary(
                '/AmericanBanks/table',
                request_serializer=american__banks__pb2.AmericanBanksTableRequest.SerializeToString,
                response_deserializer=american__banks__pb2.AmericanBanksTableResponse.FromString,
                )
        self.get_all = channel.unary_unary(
                '/AmericanBanks/get_all',
                request_serializer=american__banks__pb2.AmericanBankEmpty.SerializeToString,
                response_deserializer=american__banks__pb2.AmericanBanksMultipleResponse.FromString,
                )
        self.get = channel.unary_unary(
                '/AmericanBanks/get',
                request_serializer=american__banks__pb2.AmericanBankIdRequest.SerializeToString,
                response_deserializer=american__banks__pb2.AmericanBanksResponse.FromString,
                )
        self.save = channel.unary_unary(
                '/AmericanBanks/save',
                request_serializer=american__banks__pb2.AmericanBankNotIdRequest.SerializeToString,
                response_deserializer=american__banks__pb2.AmericanBanksResponse.FromString,
                )
        self.update = channel.unary_unary(
                '/AmericanBanks/update',
                request_serializer=american__banks__pb2.AmericanBankRequest.SerializeToString,
                response_deserializer=american__banks__pb2.AmericanBanksResponse.FromString,
                )
        self.delete = channel.unary_unary(
                '/AmericanBanks/delete',
                request_serializer=american__banks__pb2.AmericanBankIdRequest.SerializeToString,
                response_deserializer=american__banks__pb2.AmericanBanksResponse.FromString,
                )


class AmericanBanksServicer(object):
    """Missing associated documentation comment in .proto file."""

    def table(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_all(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def save(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AmericanBanksServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'table': grpc.unary_unary_rpc_method_handler(
                    servicer.table,
                    request_deserializer=american__banks__pb2.AmericanBanksTableRequest.FromString,
                    response_serializer=american__banks__pb2.AmericanBanksTableResponse.SerializeToString,
            ),
            'get_all': grpc.unary_unary_rpc_method_handler(
                    servicer.get_all,
                    request_deserializer=american__banks__pb2.AmericanBankEmpty.FromString,
                    response_serializer=american__banks__pb2.AmericanBanksMultipleResponse.SerializeToString,
            ),
            'get': grpc.unary_unary_rpc_method_handler(
                    servicer.get,
                    request_deserializer=american__banks__pb2.AmericanBankIdRequest.FromString,
                    response_serializer=american__banks__pb2.AmericanBanksResponse.SerializeToString,
            ),
            'save': grpc.unary_unary_rpc_method_handler(
                    servicer.save,
                    request_deserializer=american__banks__pb2.AmericanBankNotIdRequest.FromString,
                    response_serializer=american__banks__pb2.AmericanBanksResponse.SerializeToString,
            ),
            'update': grpc.unary_unary_rpc_method_handler(
                    servicer.update,
                    request_deserializer=american__banks__pb2.AmericanBankRequest.FromString,
                    response_serializer=american__banks__pb2.AmericanBanksResponse.SerializeToString,
            ),
            'delete': grpc.unary_unary_rpc_method_handler(
                    servicer.delete,
                    request_deserializer=american__banks__pb2.AmericanBankIdRequest.FromString,
                    response_serializer=american__banks__pb2.AmericanBanksResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'AmericanBanks', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AmericanBanks(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def table(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/AmericanBanks/table',
            american__banks__pb2.AmericanBanksTableRequest.SerializeToString,
            american__banks__pb2.AmericanBanksTableResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get_all(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/AmericanBanks/get_all',
            american__banks__pb2.AmericanBankEmpty.SerializeToString,
            american__banks__pb2.AmericanBanksMultipleResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/AmericanBanks/get',
            american__banks__pb2.AmericanBankIdRequest.SerializeToString,
            american__banks__pb2.AmericanBanksResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def save(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/AmericanBanks/save',
            american__banks__pb2.AmericanBankNotIdRequest.SerializeToString,
            american__banks__pb2.AmericanBanksResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/AmericanBanks/update',
            american__banks__pb2.AmericanBankRequest.SerializeToString,
            american__banks__pb2.AmericanBanksResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/AmericanBanks/delete',
            american__banks__pb2.AmericanBankIdRequest.SerializeToString,
            american__banks__pb2.AmericanBanksResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
