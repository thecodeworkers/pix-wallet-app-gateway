from graphene import ObjectType, Field, List, String
from google.protobuf.json_format import MessageToDict
from .bank_account_controller import sender, stub
from ....types import BankAccount
from ....utils import message_error
import grpc

class BankAccountQuery(ObjectType):
    bank_accounts = List(BankAccount)

    def resolve_bank_accounts(root, info):
        try:
            request = sender.BankAccountEmpty()
            metadata = [('auth_token', '0j29BMYV64qF26vYNC4QFb6BHwF7kT')]

            response = stub.get_all(request=request, metadata=metadata)
            response = MessageToDict(response)

            if 'bankAccount' in response:
                return response['bankAccount']

            return response

        except grpc.RpcError as e:
            raise Exception(message_error(e))
