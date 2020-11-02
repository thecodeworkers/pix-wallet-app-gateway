from graphene import ObjectType, List, Field, String
from google.protobuf.json_format import MessageToDict
from .country_controller import sender, stub
from ....types import Country
from ....utils import message_error, error_log, info_log
import grpc

class CountryQuery(ObjectType):
	countries = List(Country)
	country = Field(Country, id=String(required=True))
	country_id = List(Country)

	def resolve_countries(root, info):
		try:
			request = sender.CountryEmpty()
			response = stub.get_all(request)
			response = MessageToDict(response)

			info_log(info.context.remote_addr, "consult of countries", "countries_microservice", "CountryQuery")
			if 'country' in response:
				return response['country']

			return response

		except grpc.RpcError as e:
			error_log(info.context.remote_addr, e.details(), "countries_microservice", type(e).__name__)
			raise Exception(message_error(e))
		except Exception as e:
			error_log(info.context.remote_addr, e.args[0], "bcountries_microservice", type(e).__name__)
			raise Exception(e.args[0])

	def resolve_country(root, info, id):
		try:
			request = sender.CountryIdRequest(id=id)
			response = stub.get(request)
			response = MessageToDict(response)

			info_log(info.context.remote_addr, "consult of one country", "countries_microservice", "CountryQuery")
			if 'country' in response:
				return response['country']

			return response
		except grpc.RpcError as e:
			error_log(info.context.remote_addr, e.details(), "countries_microservice", type(e).__name__)
			raise Exception(message_error(e))
		except Exception as e:
			error_log(info.context.remote_addr, e.args[0], "countries_microservice", type(e).__name__)
			raise Exception(e.args[0])