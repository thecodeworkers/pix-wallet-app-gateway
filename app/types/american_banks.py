from graphene import ObjectType, String, Float, Boolean, InputObjectType, Int

class AmericanBanks(ObjectType):
    id = String()
    routingNumber = String()
    bankName = String()
    fullName = String()
    swift = String()
    ach = String()
    numberAccount = String()
    type = String()
    documentIdentification = String()
    currency = String()
 