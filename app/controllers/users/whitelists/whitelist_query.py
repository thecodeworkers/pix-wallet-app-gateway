from graphene import ObjectType, Field, List, String
from google.protobuf.json_format import MessageToDict
from .whitelist_controller import sender, stub
from ....types import Whitelist
from ....utils import message_error, error_log, info_log
import grpc

class WhitelistQuery(ObjectType):
    whitelists = List(Whitelist)

    def resolve_whitelists(root, info):
        try:
            auth_token = info.context.headers.get('Authorization')

            request = sender.WhitelistEmpty()
            metadata = [('auth_token', '8wCxHcpGA0Q0QewGDOCsMKfbtnXMYb')]

            response = stub.get_all(request=request, metadata=metadata)
            response = MessageToDict(response)

            info_log(info.context.remote_addr, "Consult Whitelists", "users_microservice", "WhitelistQuery")
            if 'whitelist' in response:
                return response['whitelist']

            return response

        except grpc.RpcError as e:
            error_log(info.context.remote_addr, e.details(), "users_microservice", type(e).__name__)
            raise Exception(message_error(e))
        except Exception as e:
            error_log(info.context.remote_addr, e.args[0], "users_microservice", type(e).__name__)
            raise Exception(e.args[0])
