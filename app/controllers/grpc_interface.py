from ..protos import currency_pb2, currency_pb2_grpc, price_pb2, price_pb2_grpc
from ..bootstrap import init_server

resources_host = 'localhost:50051'
providers_host = 'localhost:50052'

microservices = {
    'resources': {
        'services': {
            'currencies': {
                'stub': currency_pb2_grpc.CurrencyStub(init_server(resources_host)),
                'sender': currency_pb2
            }
        }
    },
    'providers': {
        'services': {
            'prices': {
                'stub': price_pb2_grpc.PriceStub(init_server(providers_host)),
                'sender': price_pb2
            }
        }
    }
}
