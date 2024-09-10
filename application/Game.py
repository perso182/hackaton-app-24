from fetch_quote import *
from QuoteContext import *
class Game:
    def __init__(self, rounds: int) -> None:
        self.rounds = rounds
        self.current_quote = 0
        self.current_round = 0
        self.score = 0
    
    def next_round(self):
        q = get_quote()
        self.current_quote = q
        if self.current_round <= self.rounds:
            self.current_round += 1
        return q.quote
        # Returnerar nästa quotecontext och incremnterar current round
        return 
    
    def check_answer(self, answer: str):
        match answer:
            case 1: 
                if(self.current_quote.source.lower() == "Breaking Bad".lower()):
                    self.score += 1
                    return True
                else:
                    return False
            case 2: 
                if(self.current_quote.source.lower() == "Stranger Things".lower()):
                    self.score += 1
                    return True
                else:
                    return False   
            case 3: 
                if(self.current_quote.source.lower() == "Game of Thrones".lower()):
                    self.score += 1
                    return True
                else:
                    return False
            case _:
                print("Felaktig input.")
        # Ta in svaret och rättar det. ökar score med 1 om rätt
        return
    
    def get_current_round(self):
        return self.current_round
    
    def get_max_rounds(self):
        return self.rounds
    
    def get_score(self):
        return self.score

    def get_correct_source(self):
        return self.current_quote.source
    
    def get_author_of_quote(self):
        return self.current_quote.author
    
    def check_answer_online(self, answer: str):
        if answer.lower() == self.current_quote.source.lower():
            self.score += 1
            return True
        else:
            return False

    def restart_game(self):
        self.score = 0
        self.current_round = 0