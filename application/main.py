import requests
from fetch_quote import *
from QuoteContext import *
q = get_quote()

print(q.source)

answer = input("Gissa från vilken serie detta citat är: \n" + "\"" + q.quote + "\"\n" + "1: Breaking Bad\n 2: Stranger Things \n3: Game of Thrones. \n")

correct_answer = q.source

def print_output(author, truth_value):
    if(truth_value == True):
        print("Rätt svar!, Author: " + author)
    else:
        print("Fel svar!")


match answer.lower().strip():
    case "1": 
        truth_value = (correct_answer.lower() == "Breaking Bad".lower()) 
        print_output(q.author, truth_value)
    case "2": 
        truth_value = correct_answer.lower() == "Stranger Things".lower() 
        print_output(q.author, truth_value)    
    case "3": 
        truth_value = correct_answer.lower() == "Game of Thrones".lower()
        print_output(q.author, truth_value)
    case _:
        print("Felaktig input.")
#if answer.lower().strip() == q.source.lower().strip():
#    print("Rätt svar!, Author: " + q.author)
#else:
#    print("Fel svar!")

