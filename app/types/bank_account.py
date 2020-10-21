from graphene import *

class BankAccount(ObjectType):
    id = String()
    chase = String()
    branchAddress = String()
    checkingAccount = String()
    routingNumber = String()
    bank = String()

class BankAccountNotIdInput(InputObjectType):
    chase = String(required=True)
    branchAddress = String(required=True)
    checkingAccount = String(required=True)
    routingNumber = String(required=True)
    bank = String(required=True)

class BankAccountInput(BankAccountNotIdInput):
    id = String(required=True)
