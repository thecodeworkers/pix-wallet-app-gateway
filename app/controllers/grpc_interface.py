from ..protos import currency_pb2, currency_pb2_grpc
from ..bootstrap import init_server

resources_host = 'localhost:50051'

microservices = {
    'resources': {
        'services': {
            'currencies': {
                'stub': currency_pb2_grpc.CurrencyStub(init_server(resources_host)),
                'sender': currency_pb2
            }
        }
    }
}
