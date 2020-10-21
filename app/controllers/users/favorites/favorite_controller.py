from ...controller import GrpcConnect

favorites_grpc = GrpcConnect('users', 'favorites')
sender = favorites_grpc.sender
stub = favorites_grpc.stub
