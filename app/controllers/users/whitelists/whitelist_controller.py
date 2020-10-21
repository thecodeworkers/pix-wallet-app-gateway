from ...controller import GrpcConnect

whitelists_grpc = GrpcConnect('users', 'whitelists')
sender = whitelists_grpc.sender
stub = whitelists_grpc.stub
