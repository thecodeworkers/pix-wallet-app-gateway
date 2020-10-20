from ..protos import *
from ..bootstrap import init_server
from ..constants import RESOURCES_HOST, PROVIDERS_HOST, COUNTRIES_HOST, BANKS_HOST

resources_host = RESOURCES_HOST
providers_host = PROVIDERS_HOST
countries_host = COUNTRIES_HOST
banks_host = BANKS_HOST

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
    'countries': {
        'services': {
            'countries': {
                'stub': country_pb2_grpc.CountryStub(init_server(countries_host)),
                'sender': country_pb2
            }
        }
    },
    'banks': {
        'services': {
            'american_banks': {
                'stub': american_banks_pb2_grpc.AmericanBanksStub(init_server(banks_host)),
                'sender': american_banks_pb2
            }
        }
    },
    'users': {
        'services': {
            'services': {
                'bank_accounts': {
                    # 'stub': bank_account_pb2_grpc,
                    # 'sender': bank_account_pb2
                },
                'favorites': {
                    # 'stub': favorite_pb2_grpc,
                    # 'sender': favorite_pb2
                },
                'whitelists': {
                    # 'stub': whitelist_pb2_grpc,
                    # 'sender': whitelist_pb2
                }
            }
        }
    }
}
