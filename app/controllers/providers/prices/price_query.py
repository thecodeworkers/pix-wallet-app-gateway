from graphene import ObjectType, Field, List, String
from google.protobuf.json_format import MessageToDict
from .price_controller import sender, stub
from ....types import Price
import grpc

class PriceQuery(ObjectType):
    prices = List(Price)

    def resolve_prices(root, info):
        request = sender.PriceRequest(exchange='binance')
        response = stub.get_all(request)
        response = MessageToDict(response)
        
        return response['prices']
