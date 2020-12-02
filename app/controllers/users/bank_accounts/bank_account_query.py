from graphene import ObjectType, Field, List, String
from google.protobuf.json_format import MessageToDict
from .bank_account_controller import sender, stub
from ....utils import message_error, error_log, info_log
from ....types import BankAccount
import grpc

class BankAccountQuery(ObjectType):
    bank_accounts = List(BankAccount)

    def resolve_bank_accounts(root, info):
        try:
            auth_token = info.context.headers.get('Authorization')

            request = sender.BankAccountEmpty()
            metadata = [('auth_token', '8wCxHcpGA0Q0QewGDOCsMKfbtnXMYb')]

            response = stub.get_all(request=request, metadata=metadata)
            response = MessageToDict(response)

            info_log(info.context.remote_addr, 'Consult of Bank Accounts', 'users_microservice', 'BankAccountQuery')
            if 'bankAccount' in response:
                return response['bankAccount']

            return response

        except grpc.RpcError as e:
            error_log(info.context.remote_addr, e.details(), 'users_microservice', type(e).__name__)
            raise Exception(message_error(e))
        except Exception as e:
            error_log(info.context.remote_addr, e.args[0], 'users_microservice', type(e).__name__)
            raise Exception(e.args[0])
