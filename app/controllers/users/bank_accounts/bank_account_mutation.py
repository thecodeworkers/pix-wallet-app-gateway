from graphene import ObjectType, Field, List, Mutation, String, Boolean
from google.protobuf.json_format import MessageToDict
from .bank_account_controller import sender, stub
from ....types import BankAccount, BankAccountInput, BankAccountNotIdInput
from ....utils import message_error, error_log, info_log
import grpc

class CreateBankAccount(Mutation):
    class Arguments:
        bank_account_data = BankAccountNotIdInput(required=True)

    bankAccount = Field(BankAccount)

    def mutate(self, info, bank_account_data):
        try:
            auth_token = info.context.headers.get('Authorization')

            request = sender.BankAccountNotIdRequest(**bank_account_data)
            metadata = [('auth_token', '8wCxHcpGA0Q0QewGDOCsMKfbtnXMYb')]
            response = stub.save(request=request, metadata=metadata)
            response = MessageToDict(response)

            info_log(info.context.remote_addr, 'Create Bank Account', 'users_microservice', 'CreateBankAccount')
            return CreateBankAccount(**response)

        except grpc.RpcError as e:
            error_log(info.context.remote_addr, e.details(), 'users_microservice', type(e).__name__)
            raise Exception(message_error(e))
        except Exception as e:
            error_log(info.context.remote_addr, e.args[0], 'users_microservice', type(e).__name__)
            raise Exception(e.args[0])

class UpdateBankAccount(Mutation):
    class Arguments:
        bank_account_data = BankAccountInput(required=True)

    bankAccount = Field(BankAccount)

    def mutate(self, info, bank_account_data):
        try:
            auth_token = info.context.headers.get('Authorization')

            request = sender.BankAccountRequest(**bank_account_data)
            metadata = [('auth_token', '8wCxHcpGA0Q0QewGDOCsMKfbtnXMYb')]
            response = stub.update(request=request, metadata=metadata)
            response = MessageToDict(response)

            info_log(info.context.remote_addr, 'Update Bank Account', 'users_microservice', 'UpdateBankAccount')
            return CreateBankAccount(**response)

        except grpc.RpcError as e:
            error_log(info.context.remote_addr, e.details(), 'users_microservice', type(e).__name__)
            raise Exception(message_error(e))
        except Exception as e:
            error_log(info.context.remote_addr, e.args[0], 'users_microservice', type(e).__name__)
            raise Exception(e.args[0])

class DeleteBankAccount(Mutation):
    class Arguments:
        id = String(required=True)

    ok = Boolean()

    def mutate(self, info, id):
        try:
            auth_token = info.context.headers.get('Authorization')

            request = sender.BankAccountIdRequest(id=id)
            metadata = [('auth_token', '8wCxHcpGA0Q0QewGDOCsMKfbtnXMYb')]

            stub.delete(request=request, metadata=metadata)

            info_log(info.context.remote_addr, 'Delete Bank Account', 'users_microservice', 'DeleteBankAccount')
            return DeleteBankAccount(ok=True)

        except grpc.RpcError as e:
            error_log(info.context.remote_addr, e.details(), 'users_microservice', type(e).__name__)
            raise Exception(message_error(e))
        except Exception as e:
            error_log(info.context.remote_addr, e.args[0], 'users_microservice', type(e).__name__)
            raise Exception(e.args[0])

class BankAccountMutation(ObjectType):
    create_bank_account = CreateBankAccount.Field()
    update_bank_account = UpdateBankAccount.Field()
    delete_bank_account = DeleteBankAccount.Field()
