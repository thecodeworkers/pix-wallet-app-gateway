from graphene import ObjectType, String, Float, Boolean

class Currency(ObjectType):
    name = String()
    color = String()
    active = Boolean()
    type = String()
    symbol = String()
    price = Float()
