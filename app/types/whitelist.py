from graphene import ObjectType, String, InputObjectType

class Whitelist(ObjectType):
    id = String()
    address = String()
    currency = String()

class WhitelistNotIdInput(InputObjectType):
    address = String(required=True)
    currency = String(required=True)

class WhitelistInput(WhitelistNotIdInput):
    id = String(required=True)
