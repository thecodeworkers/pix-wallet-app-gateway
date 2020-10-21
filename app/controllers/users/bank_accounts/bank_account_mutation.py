from graphene import ObjectType, Field, List, Mutation, String, Boolean
from google.protobuf.json_format import MessageToDict
from .bank_account_controller import sender, stub
from ....types import BankAccount, BankAccountInput, BankAccountNotIdInput
from ....utils import message_error
import grpc

class CreateBankAccount(Mutation):
    class Arguments:
        bank_account_data = BankAccountNotIdInput(required=True)

    bankAccount = Field(BankAccount)

    def mutate(self, info, bank_account_data):
        try:
            request = sender.BankAccountNotIdRequest(**bank_account_data)
            metadata = [('auth_token', '0j29BMYV64qF26vYNC4QFb6BHwF7kT')]
            response = stub.save(request=request, metadata=metadata)
            response = MessageToDict(response)

            return CreateBankAccount(**response)

        except grpc.RpcError as e:
            raise Exception(message_error(e))

class UpdateBankAccount(Mutation):
    class Arguments:
        bank_account_data = BankAccountInput(required=True)

    bankAccount = Field(BankAccount)

    def mutate(self, info, bank_account_data):
        try:
            request = sender.BankAccountRequest(**bank_account_data)
            metadata = [('auth_token', '0j29BMYV64qF26vYNC4QFb6BHwF7kT')]
            response = stub.update(request=request, metadata=metadata)
            response = MessageToDict(response)

            return CreateBankAccount(**response)

        except grpc.RpcError as e:
            raise Exception(message_error(e))

class DeleteBankAccount(Mutation):
    class Arguments:
        id = String(required=True)

    ok = Boolean()

    def mutate(self, info, id):
        try:
            request = sender.BankAccountIdRequest(id=id)
            metadata = [('auth_token', '0j29BMYV64qF26vYNC4QFb6BHwF7kT')]

            stub.delete(request=request, metadata=metadata)

            return DeleteBankAccount(ok=True)

        except grpc.RpcError as e:
            raise Exception(message_error(e))

class BankAccountMutation(ObjectType):
    create_bank_account = CreateBankAccount.Field()
    update_bank_account = UpdateBankAccount.Field()
    delete_bank_account = DeleteBankAccount.Field()
