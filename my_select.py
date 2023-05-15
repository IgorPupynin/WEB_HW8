import sys
import json
from pymongo import MongoClient
from mongoengine import connect
from model import Author, Quote

client = MongoClient("mongodb+srv://userweb10:567234@sandbox.n44nvce.mongodb.net/?retryWrites=true&w=majority")
db = client.web10
connect('web10', host="mongodb+srv://userweb10:567234@sandbox.n44nvce.mongodb.net/web10?retryWrites=true&w=majority")


def search_quotes(command):
    if command.startswith('name:'):
        author_name = command.split(':')[1]
        author = Author.objects(fullname=author_name).first()
        if author:
            quotes = Quote.objects(author=author)
            print_quotes(quotes)
        else:
            print("Автор не найден.")
    elif command.startswith('tag:'):
        tag = command.split(':')[1]
        quotes = Quote.objects(tags=tag)
        print_quotes(quotes)
    elif command.startswith('tags:'):
        tags = command.split(':')[1].split(',')
        quotes = Quote.objects(tags__in=tags)
        print_quotes(quotes)
    elif command == 'exit':
        sys.exit()
    else:
        print("Неправильный формат команды.")


def print_quotes(quotes):
    for quote in quotes:
        print("Автор:", quote.author.fullname)
        print("Цитата:", quote.quote)
        print()


if __name__ == '__main__':
    while True:
        user_input = input("Введите команду: ")
        search_quotes(user_input)
