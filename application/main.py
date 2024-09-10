import requests
from fetch_quote import *
from QuoteContext import *
q = get_quote()

answer = input("Gissa från vilken serie detta citat är: \n" + "\"" + q.quote + "\"\n")


if answer.lower().strip() == q.source.lower().strip():
    print("Rätt svar!, Author: " + q.author)
else:
    print("Fel svar!")

