from graphene import ObjectType, List
from google.protobuf.json_format import MessageToDict
from .country_controller import sender, stub
from ....types import Country
from ....utils import message_error
import grpc

class CountryQuery(ObjectType):
	countries = List(Country)

	def resolve_countries(root, info):
		try:
			request = sender.CountryEmpty()
			print(request)
			response = stub.get_all(request)
			response = MessageToDict(response)

			if 'country' in response:
				return response['country']

			return response

		except grpc.RpcError as e:
			print(e)
			raise Exception(message_error(e))