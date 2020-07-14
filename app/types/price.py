from graphene import ObjectType, String, Float, Boolean, InputObjectType

class Price(ObjectType):
    currency = String()
    price = String()
