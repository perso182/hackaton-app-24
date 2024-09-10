from QuoteContext import *
import requests

def get_bb_quote() -> QuoteContext:
    r = requests.get('https://api.breakingbadquotes.xyz/v1/quotes').json()[0]
    q = QuoteContext(r['quote'], r['author'], 'Breaking bad')
    return q 

def get_stranger_things_quote() -> QuoteContext:
    uri = 'https://strangerthings-quotes.vercel.app/api/quotes'
    r = requests.get(uri).json()[0]
    q = QuoteContext(r['quote'], r['author'], 'Stranger Things')
    return q