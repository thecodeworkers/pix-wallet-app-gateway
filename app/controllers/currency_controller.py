from graphene import ObjectType, Schema, Field, List, Mutation, String
from ..types import Currency

currency_list = [
    {
        'name': 'Bitcoin',
        'symbol': 'BTC',
        'price': '9100'
    },
    {
        'name': 'Ethereum',
        'symbol': 'ETH',
        'price': '235'
    }
]

currency_dict = currency_list[0]

class Query(ObjectType):
    currencies = List(Currency)

    def resolve_currencies(root, info):
        return currency_list

class AddCurrency(Mutation):
    class Arguments:
        name = String(required=True) 
        symbol = String(required=True) 
        price = String(required=True) 

    currency = Field(Currency)

    def mutate(self, info, name, symbol, price):
        _currency = {
            'name': name,
            'symbol': symbol,
            'price': price
        }

        return AddCurrency(currency=_currency)


class CurrencyMutation(ObjectType):
    add_currency = AddCurrency.Field()

currency_controller = Schema(query=Query, mutation=CurrencyMutation)
