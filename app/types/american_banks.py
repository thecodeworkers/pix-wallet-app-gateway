from graphene import ObjectType, String, Float, Boolean, InputObjectType, Int

class AmericanBanks(ObjectType):
    id = String()
    routingNumber = String()
    bankName = String()
    fullName = String()
    swift = String()
    numberAccount = String()
    type = String()
    currency = String()
 