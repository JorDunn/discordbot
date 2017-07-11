import json
import random
import os
from pprint import pprint

class Quotes(object):
    quotes = []
    length = None

    def __init__(self):
        random.seed(os.urandom)

    def get_quotes(self):
        quotes = []
        with open('quotes.txt') as data_file:
            for line in data_file:
                quotes.append(line)
        self.length = len(quotes) - 1
        self.quotes = quotes
        print("Quotes are ready dumb dumb!")

    def random_quote(self):
        i = random.randint(0, self.length)
        return self.quotes[i]
