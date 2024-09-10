from QuoteContext import *
import requests
import random

def get_bb_quote() -> QuoteContext:
    r = requests.get('https://api.breakingbadquotes.xyz/v1/quotes').json()[0]
    q = QuoteContext(r['quote'], r['author'], 'Breaking bad')
    return q 

def get_quote() -> QuoteContext:
    quote_list = [get_bb_quote, get_got_quote, get_stranger_things_quote]
    return random.choice(quote_list)()

def get_got_quote() -> QuoteContext:
    r = requests.get('https://api.gameofthronesquotes.xyz/v1/random').json()
    q = QuoteContext(r['sentence'], r['character']['name'], 'Game of Thrones')
    return q
    
def get_stranger_things_quote() -> QuoteContext:
    uri = 'https://strangerthings-quotes.vercel.app/api/quotes'
    r = requests.get(uri).json()[0]
    q = QuoteContext(r['quote'], r['author'], 'Stranger Things')
    return q
