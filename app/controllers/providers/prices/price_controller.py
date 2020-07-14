from ...controller import GrpcConnect

price_grpc = GrpcConnect('providers', 'prices')
sender = price_grpc.sender
stub = price_grpc.stub
