from QuoteContext import *
import requests
import random

def get_bb_quote() -> QuoteContext:
    r = requests.get('https://api.breakingbadquotes.xyz/v1/quotes').json()[0]
    q = QuoteContext(r['quote'], r['author'], 'Breaking bad')
    return q 

def get_quote() -> QuoteContext:
    quote_list = [get_bb_quote]
    return random.choice(quote_list)()