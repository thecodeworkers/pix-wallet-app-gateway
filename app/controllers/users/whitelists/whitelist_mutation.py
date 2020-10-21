from graphene import ObjectType, Field, List, Mutation, String, Boolean
from google.protobuf.json_format import MessageToDict
from .whitelist_controller import sender, stub
from ....types import Whitelist, WhitelistInput, WhitelistNotIdInput
from ....utils import message_error
import grpc

class CreateWhitelist(Mutation):
    class Arguments:
        whitelist_data = WhitelistNotIdInput(required=True)

    whitelist = Field(Whitelist)

    def mutate(self, info, whitelist_data):
        try:
            request = sender.WhitelistNotIdRequest(**whitelist_data)
            metadata = [('auth_token', '0j29BMYV64qF26vYNC4QFb6BHwF7kT')]
            response = stub.save(request=request, metadata=metadata)
            response = MessageToDict(response)

            return CreateWhitelist(**response)

        except grpc.RpcError as e:
            raise Exception(message_error(e))

class UpdateWhitelist(Mutation):
    class Arguments:
        whitelist_data = WhitelistInput(required=True)

    whitelist = Field(Whitelist)

    def mutate(self, info, whitelist_data):
        try:
            request = sender.WhitelistRequest(**whitelist_data)
            metadata = [('auth_token', '0j29BMYV64qF26vYNC4QFb6BHwF7kT')]
            response = stub.update(request=request, metadata=metadata)
            response = MessageToDict(response)

            return CreateWhitelist(**response)

        except grpc.RpcError as e:
            raise Exception(message_error(e))

class DeleteWhitelist(Mutation):
    class Arguments:
        id = String(required=True)

    ok = Boolean()

    def mutate(self, info, id):
        try:
            request = sender.WhitelistIdRequest(id=id)
            metadata = [('auth_token', '0j29BMYV64qF26vYNC4QFb6BHwF7kT')]

            stub.delete(request=request, metadata=metadata)

            return DeleteWhitelist(ok=True)

        except grpc.RpcError as e:
            raise Exception(message_error(e))

class WhitelistMutation(ObjectType):
    create_whitelist = CreateWhitelist.Field()
    update_whitelist = UpdateWhitelist.Field()
    delete_whitelist = DeleteWhitelist.Field()
