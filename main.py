import random
class RockPaperScissors:
    def __init__(self):
        self.choices = {
            1 : "rock" ,
            2 : "paper" ,
            3 : "scissors"
        }
    
    def comp_choice(self):
        return random.randint(1,3)
    
    def user_input(self):
        user = input("enter rock/paper/scissors").strip().lower()
    
        mapping = {
        "rock" : 1 ,
        "paper" : 2 ,
        "scissors" : 3
        }

        if user not in mapping:
            print("invalid input😢" )
            return None
        return mapping[user]

    def get_winner(self, user, comp):
        print("You chose" , self.choices[user])
        print("computer chose" , self.choices[comp])
        if (user == comp):
            return "Result: Draw 🤝"
        if (user == 1 and comp == 3) or \
           (user == 2 and comp == 1) or \
           (user == 3 and comp == 2):
                return "Result: You Win 🎉"
    
        return "Result: Computer Wins 💻"

    def play(self):
        user = self.user_input()
        if user is None:
            return
        comp = self.comp_choice()
        result = self.get_winner(user,comp)
        print(result)
game = RockPaperScissors()
game.play()

     



