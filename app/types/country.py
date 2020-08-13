from graphene import ObjectType, String, Boolean

class Country(ObjectType):
    id = String()
    name = String()
    phone_prefix = String()
    active = Boolean()