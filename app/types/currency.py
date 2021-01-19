from graphene import *
from .table import Table
class Currency(ObjectType):
    id = String()
    name = String()
    color = String()
    active = Boolean()
    type = String()
    symbol = String()
    price = Float()

class CurrencyTable(Table):
    items = List(Currency)