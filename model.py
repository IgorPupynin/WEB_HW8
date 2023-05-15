from pymongo import MongoClient
from mongoengine import fields, Document

client = MongoClient("mongodb+srv://userweb10:567234@sandbox.n44nvce.mongodb.net/?retryWrites=true&w=majority")
db = client.web10


class Author(Document):
    fullname = fields.StringField()
    born_date = fields.StringField()
    born_location = fields.StringField()
    description = fields.StringField()


class Quote(Document):
    tags = fields.ListField(fields.StringField())
    author = fields.ReferenceField(Author)
    quote = fields.StringField()


class Contact(Document):
    fullname = fields.StringField(required=True)
    email = fields.EmailField(required=True)
    additional_info = fields.StringField()
    is_sent = fields.BooleanField(default=False)