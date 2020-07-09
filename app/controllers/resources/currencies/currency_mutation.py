from graphene import ObjectType, Field, List, Mutation, String, Boolean
from google.protobuf.json_format import MessageToDict
from .currency_connect import sender, stub
from ....types import Currency, CurrencyInput, CurrencyNotIdInput
import grpc

class CreateCurrency(Mutation):
    class Arguments:
        currency_data = CurrencyNotIdInput(required=True)

    currency = Field(Currency)

    def mutate(self, info, currency_data=None):
        try:
            request = sender.CurrencyNotIdRequest(**currency_data)
            response = stub.save(request)
            response = MessageToDict(response)
            
            return CreateCurrency(**response)

        except grpc.RpcError as e:
            raise Exception(e.details())

class UpdateCurrency(Mutation):
    class Arguments:
        currency_data = CurrencyInput(required=True)

    currency = Field(Currency)

    def mutate(self, info, currency_data=None):
        try:
            request = sender.CurrencyRequest(**currency_data)
            response = stub.update(request)
            response = MessageToDict(response)
            
            return CreateCurrency(**response)

        except grpc.RpcError as e:
            raise Exception(e.details())

class DeleteCurrency(Mutation):
    class Arguments:
        id = String(required=True)

    ok = Boolean()

    def mutate(self, info, id):
        try:
            request = sender.CurrencyIdRequest(id=id)
            response = stub.delete(request)
        
            return DeleteCurrency(ok=True)

        except grpc.RpcError as e:
            raise Exception(e.details())

class CurrencyMutation(ObjectType):
    create_currency = CreateCurrency.Field()
    update_currency = UpdateCurrency.Field()
    delete_currency = DeleteCurrency.Field()
