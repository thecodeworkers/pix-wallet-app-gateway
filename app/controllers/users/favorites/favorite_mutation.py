from graphene import ObjectType, Field, List, Mutation, String, Boolean
from google.protobuf.json_format import MessageToDict
from .favorite_controller import sender, stub
from ....types import Favorite, FavoriteInput, FavoriteNotIdInput
from ....utils import message_error
import grpc

class CreateFavorite(Mutation):
    class Arguments:
        favorite_data = FavoriteNotIdInput(required=True)

    favorite = Field(Favorite)

    def mutate(self, info, favorite_data):
        try:
            auth_token = info.context.headers.get('Authorization')

            request = sender.FavoriteNotIdRequest(**favorite_data)
            metadata = [('auth_token', '0j29BMYV64qF26vYNC4QFb6BHwF7kT')]
            response = stub.save(request=request, metadata=metadata)
            response = MessageToDict(response)

            return CreateFavorite(**response)

        except grpc.RpcError as e:
            raise Exception(message_error(e))

class UpdateFavorite(Mutation):
    class Arguments:
        favorite_data = FavoriteInput(required=True)

    favorite = Field(Favorite)

    def mutate(self, info, favorite_data):
        try:
            auth_token = info.context.headers.get('Authorization')

            request = sender.FavoriteRequest(**favorite_data)
            metadata = [('auth_token', '0j29BMYV64qF26vYNC4QFb6BHwF7kT')]
            response = stub.update(request=request, metadata=metadata)
            response = MessageToDict(response)

            return CreateFavorite(**response)

        except grpc.RpcError as e:
            raise Exception(message_error(e))

class DeleteFavorite(Mutation):
    class Arguments:
        id = String(required=True)

    ok = Boolean()

    def mutate(self, info, id):
        try:
            auth_token = info.context.headers.get('Authorization')

            request = sender.FavoriteIdRequest(id=id)
            metadata = [('auth_token', '0j29BMYV64qF26vYNC4QFb6BHwF7kT')]

            stub.delete(request=request, metadata=metadata)

            return DeleteFavorite(ok=True)

        except grpc.RpcError as e:
            raise Exception(message_error(e))

class FavoriteMutation(ObjectType):
    create_favorite = CreateFavorite.Field()
    update_favorite = UpdateFavorite.Field()
    delete_favorite = DeleteFavorite.Field()
