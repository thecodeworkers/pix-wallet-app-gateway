# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import city_pb2 as city__pb2


class CityStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.table = channel.unary_unary(
                '/City/table',
                request_serializer=city__pb2.CityTableRequest.SerializeToString,
                response_deserializer=city__pb2.CityTableResponse.FromString,
                )
        self.get_all = channel.unary_unary(
                '/City/get_all',
                request_serializer=city__pb2.CityEmpty.SerializeToString,
                response_deserializer=city__pb2.CityMultipleResponse.FromString,
                )
        self.get = channel.unary_unary(
                '/City/get',
                request_serializer=city__pb2.CityIdRequest.SerializeToString,
                response_deserializer=city__pb2.CityResponse.FromString,
                )
        self.save = channel.unary_unary(
                '/City/save',
                request_serializer=city__pb2.CityNotIdRequest.SerializeToString,
                response_deserializer=city__pb2.CityResponse.FromString,
                )
        self.update = channel.unary_unary(
                '/City/update',
                request_serializer=city__pb2.CityRequest.SerializeToString,
                response_deserializer=city__pb2.CityResponse.FromString,
                )
        self.delete = channel.unary_unary(
                '/City/delete',
                request_serializer=city__pb2.CityIdRequest.SerializeToString,
                response_deserializer=city__pb2.CityEmpty.FromString,
                )


class CityServicer(object):
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


def add_CityServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'table': grpc.unary_unary_rpc_method_handler(
                    servicer.table,
                    request_deserializer=city__pb2.CityTableRequest.FromString,
                    response_serializer=city__pb2.CityTableResponse.SerializeToString,
            ),
            'get_all': grpc.unary_unary_rpc_method_handler(
                    servicer.get_all,
                    request_deserializer=city__pb2.CityEmpty.FromString,
                    response_serializer=city__pb2.CityMultipleResponse.SerializeToString,
            ),
            'get': grpc.unary_unary_rpc_method_handler(
                    servicer.get,
                    request_deserializer=city__pb2.CityIdRequest.FromString,
                    response_serializer=city__pb2.CityResponse.SerializeToString,
            ),
            'save': grpc.unary_unary_rpc_method_handler(
                    servicer.save,
                    request_deserializer=city__pb2.CityNotIdRequest.FromString,
                    response_serializer=city__pb2.CityResponse.SerializeToString,
            ),
            'update': grpc.unary_unary_rpc_method_handler(
                    servicer.update,
                    request_deserializer=city__pb2.CityRequest.FromString,
                    response_serializer=city__pb2.CityResponse.SerializeToString,
            ),
            'delete': grpc.unary_unary_rpc_method_handler(
                    servicer.delete,
                    request_deserializer=city__pb2.CityIdRequest.FromString,
                    response_serializer=city__pb2.CityEmpty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'City', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class City(object):
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
        return grpc.experimental.unary_unary(request, target, '/City/table',
            city__pb2.CityTableRequest.SerializeToString,
            city__pb2.CityTableResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/City/get_all',
            city__pb2.CityEmpty.SerializeToString,
            city__pb2.CityMultipleResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/City/get',
            city__pb2.CityIdRequest.SerializeToString,
            city__pb2.CityResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/City/save',
            city__pb2.CityNotIdRequest.SerializeToString,
            city__pb2.CityResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/City/update',
            city__pb2.CityRequest.SerializeToString,
            city__pb2.CityResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/City/delete',
            city__pb2.CityIdRequest.SerializeToString,
            city__pb2.CityEmpty.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
