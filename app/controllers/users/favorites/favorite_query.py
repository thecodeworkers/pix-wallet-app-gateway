from graphene import ObjectType, Field, List, String
from google.protobuf.json_format import MessageToDict
from .favorite_controller import sender, stub
from ....types import Favorite
from ....utils import message_error
import grpc

class FavoriteQuery(ObjectType):
    favorites = List(Favorite)

    def resolve_favorites(root, info):
        try:
            request = sender.FavoriteEmpty()
            metadata = [('auth_token', '0j29BMYV64qF26vYNC4QFb6BHwF7kT')]

            response = stub.get_all(request=request, metadata=metadata)
            response = MessageToDict(response)

            if 'favorite' in response:
                return response['favorite']

            return response

        except grpc.RpcError as e:
            raise Exception(message_error(e))
