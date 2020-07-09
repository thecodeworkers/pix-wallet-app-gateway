from graphene import Schema
from .currency_query import CurrencyQuery
from .currency_mutation import CurrencyMutation

currency_controller = Schema(
    query=CurrencyQuery, 
    mutation=CurrencyMutation
)
