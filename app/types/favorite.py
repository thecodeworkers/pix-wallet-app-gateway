from graphene import ObjectType, String, InputObjectType

class Favorite(ObjectType):
    id = String()
    names = String()
    username = String()

class FavoriteNotIdInput(InputObjectType):
    names = String(required=True)
    username = String(required=True)

class FavoriteInput(FavoriteNotIdInput):
    id = String(required=True)
