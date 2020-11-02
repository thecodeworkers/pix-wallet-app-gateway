from graphene import ObjectType, Field, List, String
from google.protobuf.json_format import MessageToDict
from .language_controller import sender, stub
from ....types import Language
import grpc

class LanguageQuery(ObjectType):
    languages = List(Language)

    def resolve_languages(root, info):
        try:
            request = sender.LanguageEmpty()
            response = stub.get_all(request)
            response = MessageToDict(response)
            
            info_log(info.context.remote_addr, "consult of languages", "resources_microservice", "LanguageQuery")
            if 'language' in response:
                return response['language']
            
            return response
        
        except grpc.RpcError as e:
            error_log(info.context.remote_addr, e.details(), "resources_microservice", type(e).__name__)
            raise Exception(message_error(e))
        except Exception as e:
            error_log(info.context.remote_addr, e.args[0], "resources_microservice", type(e).__name__)
            raise Exception(e.args[0])
