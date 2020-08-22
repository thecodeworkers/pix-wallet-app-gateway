import grpc
from app.protos import country_pb2, country_pb2_grpc

class CountryClient():

    def __init__(self):
        self.channel = grpc.insecure_channel('localhost:50053')
        self.stub = country_pb2_grpc.CountryStub(self.channel)

    def get_table(self, page, per_page):
        
        try:
            request_data = {
                'page': page,
                'per_page': per_page
            }

            request = country_pb2.CountryTableRequest(**request_data)

            response = self.stub.table(request)

            return response
        except grpc.RpcError as error:
            print(error.details())
            return error.details()
        except Exception as error:
            print(error)
            return error
    
    def get_all(self):
        try:
            request = country_pb2.CountryEmpty()

            response = self.stub.get_all(request)

            return response
        except grpc.RpcError as error:
            print(error.details())
            return error.details()
        except Exception as error:
            print(error)
            return error

    def get(self):
        try:

            request_data= {
                'id': '5f330b8256ad8b97a885db54'
            }

            request = country_pb2.CountryIdRequest(**request_data)

            response = self.stub.get(request)

            return response
        except grpc.RpcError as error:
            print(error.details())
            return error.details()
        except Exception as error:
            print(error)
            return error
    
    def save(self):
        try:
            request_data= {
              'name': 'NewContry',
              'phone_prefix': '+89',
              'active': 0,
              'states': [],
            }

            request = country_pb2.CountryNotIdRequest(**request_data)
            response = self.stub.save(request)

            return response
        except grpc.RpcError as error:
            print(error)
            print(error.details())
            return error.details()
        except Exception as error:
            print(error)
            return error
    
    def update(self):
        try:

            request_data= {
                'id': '5f40c38bf6d55f5123630e33',
                'name': 'NewCountry',
                'phone_prefix': '+299',
                'states': []
            }

            request = country_pb2.CountryRequest(**request_data)

            response = self.stub.update(request)

            return response
        except grpc.RpcError as error:
            print(error)
            print(error.details())
            return error.details()
        except Exception as error:
            print(error)
            return error

    def delete(self):
        try:

            request_data= {
                'id': '5f40c38bf6d55f5123630e33'
            }

            request = country_pb2.CountryIdRequest(**request_data)

            response = self.stub.delete(request)

            return response
        except grpc.RpcError as error:
            print(error.details())
            return error.details()
        except Exception as error:
            print(error)
            return error
        


client = CountryClient()

# print(client.get_table(19, 10))
# print(client.get_all())
# print(client.get())
# print(client.save())
# print(client.update())
print(client.delete())