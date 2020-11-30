from graphene import ObjectType, Field, List, Mutation, String, Boolean
from google.protobuf.json_format import MessageToDict
from .favorite_controller import sender, stub
from ....types import Favorite, FavoriteInput, FavoriteNotIdInput
from ....utils import message_error, error_log, info_log
import grpc

class CreateFavorite(Mutation):
    class Arguments:
        favorite_data = FavoriteNotIdInput(required=True)

    favorite = Field(Favorite)

    def mutate(self, info, favorite_data):
        try:
            auth_token = info.context.headers.get('Authorization')

            request = sender.FavoriteNotIdRequest(**favorite_data)
            metadata = [('auth_token', '8wCxHcpGA0Q0QewGDOCsMKfbtnXMYb')]
            response = stub.save(request=request, metadata=metadata)
            response = MessageToDict(response)

            info_log(info.context.remote_addr, 'Create Favorite', 'users_microservice', 'CreateFavorite')
            return CreateFavorite(**response)

        except grpc.RpcError as e:
            error_log(info.context.remote_addr, e.details(), 'users_microservice', type(e).__name__)
            raise Exception(message_error(e))
        except Exception as e:
            error_log(info.context.remote_addr, e.args[0], 'users_microservice', type(e).__name__)
            raise Exception(e.args[0])
class UpdateFavorite(Mutation):
    class Arguments:
        favorite_data = FavoriteInput(required=True)

    favorite = Field(Favorite)

    def mutate(self, info, favorite_data):
        try:
            auth_token = info.context.headers.get('Authorization')

            request = sender.FavoriteRequest(**favorite_data)
            metadata = [('auth_token', '8wCxHcpGA0Q0QewGDOCsMKfbtnXMYb')]
            response = stub.update(request=request, metadata=metadata)
            response = MessageToDict(response)

            info_log(info.context.remote_addr, 'Update Favorite', 'users_microservice', 'UpdateFavorite')
            return CreateFavorite(**response)

        except grpc.RpcError as e:
            error_log(info.context.remote_addr, e.details(), 'users_microservice', type(e).__name__)
            raise Exception(message_error(e))
        except Exception as e:
            error_log(info.context.remote_addr, e.args[0], 'users_microservice', type(e).__name__)
            raise Exception(e.args[0])

class DeleteFavorite(Mutation):
    class Arguments:
        id = String(required=True)

    ok = Boolean()

    def mutate(self, info, id):
        try:
            auth_token = info.context.headers.get('Authorization')

            request = sender.FavoriteIdRequest(id=id)
            metadata = [('auth_token', '8wCxHcpGA0Q0QewGDOCsMKfbtnXMYb')]

            stub.delete(request=request, metadata=metadata)

            info_log(info.context.remote_addr, 'Delete Favorite', 'users_microservice', 'DeleteFavorite')
            return DeleteFavorite(ok=True)

        except grpc.RpcError as e:
            error_log(info.context.remote_addr, e.details(), 'users_microservice', type(e).__name__)
            raise Exception(message_error(e))
        except Exception as e:
            error_log(info.context.remote_addr, e.args[0], 'users_microservice', type(e).__name__)
            raise Exception(e.args[0])

class FavoriteMutation(ObjectType):
    create_favorite = CreateFavorite.Field()
    update_favorite = UpdateFavorite.Field()
    delete_favorite = DeleteFavorite.Field()
