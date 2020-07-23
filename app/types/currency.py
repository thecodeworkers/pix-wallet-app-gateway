from graphene import ObjectType, String, Float, Boolean, InputObjectType, Int


class Currency(ObjectType):
    id = String()
    name = String()
    color = String()
    active = Boolean()
    type = String()
    symbol = String()
    price = Float()

class CurrencyNotIdInput(InputObjectType):
    name = String(required=True)
    color = String(required=True)
    active = Boolean()
    type = Int(required=True)
    symbol = String(required=True)
    price = Float(required=True)

class CurrencyInput(CurrencyNotIdInput):
    id = String(required=True)
