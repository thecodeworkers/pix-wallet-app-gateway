from graphene import ObjectType, String, Float, Boolean, InputObjectType, Int


class Currency(ObjectType):
    id = String()
    name = String()
    color = String()
    active = Boolean()
    type = String()
    symbol = String()
    price = Float()
