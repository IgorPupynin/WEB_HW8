import json
from pymongo import MongoClient
from mongoengine import connect
from model import Author, Quote

client = MongoClient("mongodb+srv://userweb10:567234@sandbox.n44nvce.mongodb.net/?retryWrites=true&w=majority")
db = client.web10
connect(host="mongodb+srv://userweb10:567234@sandbox.n44nvce.mongodb.net/web10?retryWrites=true&w=majority")


if __name__ == '__main__':
    
    with open('authors.json', 'r') as file:
        authors_data = json.load(file)

    with open('quotes.json', 'r') as file:
        quotes_data = json.load(file)

    for author_data in authors_data:
        author = Author(**author_data)
        author.save()

    for quote_data in quotes_data:
        author_fullname = quote_data['author']
        author = Author.objects(fullname=author_fullname).first()
        if author:
            quote_data['author'] = author
            quote = Quote(**quote_data)
            quote.save()

    client.close()
