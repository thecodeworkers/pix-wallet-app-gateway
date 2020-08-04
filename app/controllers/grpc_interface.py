from ..protos import currency_pb2, currency_pb2_grpc, language_pb2, language_pb2_grpc
from ..bootstrap import init_server

resources_host = 'micro_resources:50051'
providers_host = 'micro_providers:50052'

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
