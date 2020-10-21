from graphene import ObjectType, Field, List, String
from google.protobuf.json_format import MessageToDict
from .whitelist_controller import sender, stub
from ....types import Whitelist
from ....utils import message_error
import grpc

class WhitelistQuery(ObjectType):
    whitelists = List(Whitelist)

    def resolve_whitelists(root, info):
        try:
            request = sender.WhitelistEmpty()
            metadata = [('auth_token', '0j29BMYV64qF26vYNC4QFb6BHwF7kT')]

            response = stub.get_all(request=request, metadata=metadata)
            response = MessageToDict(response)

            if 'whitelist' in response:
                return response['whitelist']

            return response

        except grpc.RpcError as e:
            raise Exception(message_error(e))
