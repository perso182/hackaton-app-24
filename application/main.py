import requests
from fetch_quote import *
from QuoteContext import *
from Game import *
#q = get_quote()

#print(q.source)

#answer = input("Gissa från vilken serie detta citat är: \n" + "\"" + q.quote + "\"\n" + "1: Breaking Bad\n2: Stranger Things \n3: Game of Thrones. \n")

nr_of_rounds = 3
game = Game(nr_of_rounds)

while game.get_current_round() < game.get_max_rounds():
    quote = game.next_round()
    answer = input("Gissa från vilken serie detta citat är: \n" + "\"" + quote + "\"\n" + "1: Breaking Bad\n2: Stranger Things \n3: Game of Thrones. \n")
    if game.check_answer(int(answer)):
        print("Rätt! Author: " + game.get_author_of_quote())
    else:
        print("FEL! Rätt svar är: " + game.get_correct_source())

print("Score: " + str(game.get_score()))




#correct_answer = q.source

def print_output(author, truth_value):
    if(truth_value == True):
        print("Rätt svar!, Author: " + author)
    else:
        print("Fel svar!")


