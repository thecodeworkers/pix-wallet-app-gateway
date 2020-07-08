from flask_graphql import GraphQLView
from ..bootstrap import app
from ..controllers import currency_controller

def graphql_routes():
    app.add_url_rule('/graphql/currencies', view_func=GraphQLView.as_view('currencies', schema=currency_controller, graphiql=True))
