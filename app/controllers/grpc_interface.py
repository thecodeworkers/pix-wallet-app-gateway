from ..protos import currency_pb2, currency_pb2_grpc, american_banks_pb2, american_banks_pb2_grpc, language_pb2_grpc, language_pb2
from ..bootstrap import init_server

resources_host = 'localhost:50051'
providers_host = 'localhost:50052'
american_banks_host = 'localhost:50053'

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
    },

    'banks': {
        'services': {
            'american_banks': {
                'stub': american_banks_pb2_grpc.AmericanBanksStub(init_server(american_banks_host)),
                'sender': american_banks_pb2
            }
        }
    }
}
