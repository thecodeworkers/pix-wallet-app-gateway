from graphene import ObjectType, String, Float, Boolean, InputObjectType, List
from .table import Table
class Language(ObjectType):
    id = String()
    name = String()
    prefix = String()
    active = Boolean()
class LanguageTable(Table):
    items = List(Language)
