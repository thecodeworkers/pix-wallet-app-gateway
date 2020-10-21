from ..bootstrap import init_server
from ..constants import *
from ..protos import *

microservices = {
    'resources': {
        'services': {
            'currencies': {
                'stub': currency_pb2_grpc.CurrencyStub(init_server(RESOURCES_HOST)),
                'sender': currency_pb2
            },
            'languages': {
                'stub': language_pb2_grpc.LanguageStub(init_server(RESOURCES_HOST)),
                'sender': language_pb2
            }
        }
    },
    'countries': {
        'services': {
            'countries': {
                'stub': country_pb2_grpc.CountryStub(init_server(COUNTRIES_HOST)),
                'sender': country_pb2
            }
        }
    },
    'banks': {
        'services': {
            'american_banks': {
                'stub': american_banks_pb2_grpc.AmericanBanksStub(init_server(BANKS_HOST)),
                'sender': american_banks_pb2
            }
        }
    },
    'users': {
        'services': {
            'bank_accounts': {
                'stub': bank_account_pb2_grpc.BankAccountStub(init_server(USERS_HOST)),
                'sender': bank_account_pb2
            },
            'favorites': {
                'stub': favorite_pb2_grpc.FavoriteStub(init_server(USERS_HOST)),
                'sender': favorite_pb2
            },
            'whitelists': {
                'stub': whitelist_pb2_grpc.WhitelistStub(init_server(USERS_HOST)),
                'sender': whitelist_pb2
            }
        }
    }
}
