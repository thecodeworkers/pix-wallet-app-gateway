from ...controller import GrpcConnect

american_banks_grpc = GrpcConnect('banks', 'american_banks')
sender = american_banks_grpc.sender
stub = american_banks_grpc.stub
