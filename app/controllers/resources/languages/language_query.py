from graphene import ObjectType, Field, List, String
from google.protobuf.json_format import MessageToDict
from .language_controller import sender, stub
from ....types import Language
import grpc

class LanguageQuery(ObjectType):
    languages = List(Language)
    language = Field(Language, id=String(required=True))

    def resolve_languages(root, info):
        try:
            request = sender.LanguageEmpty()
            response = stub.get_all(request)
            response = MessageToDict(response)
            
            if 'language' in response:
                return response['language']
            
            return response
        
        except grpc.RpcError as e:
            raise Exception(e.details())

    def resolve_language(root, info, id):
        try:
            request = sender.LanguageIdRequest(id=id)
            response = stub.get(request)
            response = MessageToDict(response)

            if 'language' in response:
                return response['language']
        
            return response
        
        except grpc.RpcError as e:
            raise Exception(e.details())
