from ..protos import currency_pb2, currency_pb2_grpc, language_pb2, language_pb2_grpc
from ..bootstrap import init_server

resources_host = '200.0.0.22:50051'
providers_host = '200.0.0.21:50052'

microservices = {
    'resources': {
        'services': {
            'currencies': {
                'stub': currency_pb2_grpc.CurrencyStub(init_server(resources_host)),
                'sender': currency_pb2
            },
            'languages': {
                'stub': language_pb2_grpc.LanguageStub(init_server(resources_host)),
                'sender': language_pb2
            }
        }
    }
}
