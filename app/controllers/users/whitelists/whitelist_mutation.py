from graphene import ObjectType, Field, List, Mutation, String, Boolean
from google.protobuf.json_format import MessageToDict
from .whitelist_controller import sender, stub
from ....types import Whitelist, WhitelistInput, WhitelistNotIdInput
from ....utils import message_error, error_log, info_log
import grpc

class CreateWhitelist(Mutation):
    class Arguments:
        whitelist_data = WhitelistNotIdInput(required=True)

    whitelist = Field(Whitelist)

    def mutate(self, info, whitelist_data):
        try:
            auth_token = info.context.headers.get('Authorization')

            request = sender.WhitelistNotIdRequest(**whitelist_data)
            metadata = [('auth_token', '8wCxHcpGA0Q0QewGDOCsMKfbtnXMYb')]
            response = stub.save(request=request, metadata=metadata)
            response = MessageToDict(response)

            info_log(info.context.remote_addr, "Create Whitelist", "users_microservice", "CreateWhitelist")
            return CreateWhitelist(**response)

        except grpc.RpcError as e:
            error_log(info.context.remote_addr, e.details(), "users_microservice", type(e).__name__)
            raise Exception(message_error(e))
        except Exception as e:
            error_log(info.context.remote_addr, e.args[0], "users_microservice", type(e).__name__)
            raise Exception(e.args[0])

class UpdateWhitelist(Mutation):
    class Arguments:
        whitelist_data = WhitelistInput(required=True)

    whitelist = Field(Whitelist)

    def mutate(self, info, whitelist_data):
        try:
            auth_token = info.context.headers.get('Authorization')

            request = sender.WhitelistRequest(**whitelist_data)
            metadata = [('auth_token', '8wCxHcpGA0Q0QewGDOCsMKfbtnXMYb')]
            response = stub.update(request=request, metadata=metadata)
            response = MessageToDict(response)

            info_log(info.context.remote_addr, "Update Whitelist", "users_microservice", "UpdateWhitelist")
            return CreateWhitelist(**response)

        except grpc.RpcError as e:
            error_log(info.context.remote_addr, e.details(), "users_microservice", type(e).__name__)
            raise Exception(message_error(e))
        except Exception as e:
            error_log(info.context.remote_addr, e.args[0], "users_microservice", type(e).__name__)
            raise Exception(e.args[0])

class DeleteWhitelist(Mutation):
    class Arguments:
        id = String(required=True)

    ok = Boolean()

    def mutate(self, info, id):
        try:
            auth_token = info.context.headers.get('Authorization')

            request = sender.WhitelistIdRequest(id=id)
            metadata = [('auth_token', '8wCxHcpGA0Q0QewGDOCsMKfbtnXMYb')]

            stub.delete(request=request, metadata=metadata)

            info_log(info.context.remote_addr, "Delete Whitelist", "users_microservice", "DeleteWhitelist")
            return DeleteWhitelist(ok=True)

        except grpc.RpcError as e:
            error_log(info.context.remote_addr, e.details(), "users_microservice", type(e).__name__)
            raise Exception(message_error(e))
        except Exception as e:
            error_log(info.context.remote_addr, e.args[0], "users_microservice", type(e).__name__)
            raise Exception(e.args[0])

class WhitelistMutation(ObjectType):
    create_whitelist = CreateWhitelist.Field()
    update_whitelist = UpdateWhitelist.Field()
    delete_whitelist = DeleteWhitelist.Field()
