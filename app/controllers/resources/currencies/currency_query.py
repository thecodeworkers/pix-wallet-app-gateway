from graphene import ObjectType, Field, List, String
from google.protobuf.json_format import MessageToDict
from .currency_controller import sender, stub
from ....types import Currency
import grpc

class CurrencyQuery(ObjectType):
    currencies = List(Currency)
    currency = Field(Currency, id=String(required=True))

    def resolve_currencies(root, info):
        request = sender.CurrencyEmpty()
        response = stub.get_all(request)
        response = MessageToDict(response)
        
        if 'currency' in response:
            return response['currency']
        
        return response

    def resolve_currency(root, info, id):
        try:
            request = sender.CurrencyIdRequest(id=id)
            response = stub.get(request)
            response = MessageToDict(response)

            if 'currency' in response:
                return response['currency']
        
            return response
        
        except grpc.RpcError as e:
            raise Exception(e.details())
