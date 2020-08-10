from graphene import ObjectType, Field, List, String
from google.protobuf.json_format import MessageToDict
from .american_banks_controller import sender, stub
from ....types import Banks
from ....utils import message_error
import grpc

class AmericanBanksQuery(ObjectType):
    american_banks = List(Banks)
    american_banks = Field(Banks, id=String(required=True))

    def resolve_currencies(root, info):
        try:
            request = sender.AmericanBankEmpty()
            response = stub.get_all(request)
            response = MessageToDict(response)
            
            if 'american_banks' in response:
                return response['american_banks']
            
            return response
        
        except grpc.RpcError as e:
            raise Exception(message_error(e))

    def resolve_currency(root, info, id):
        try:
            request = sender.AmericanBankIdRequest(id=id)
            response = stub.get(request)
            response = MessageToDict(response)

            if 'american_banks' in response:
                return response['american_banks']
        
            return response
        
        except grpc.RpcError as e:
            raise Exception(message_error(e))
