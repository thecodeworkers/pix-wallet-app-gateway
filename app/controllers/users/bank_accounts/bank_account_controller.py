from ...controller import GrpcConnect

bank_accounts_grpc = GrpcConnect('users', 'bank_accounts')
sender = bank_accounts_grpc.sender
stub = bank_accounts_grpc.stub
