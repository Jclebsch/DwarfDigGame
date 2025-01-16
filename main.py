from functions import game
from rank import display_top_10

user = ""

while True:
    print("---------------------------------------")
    print("---------------------------------------")
    print("   Welcome to the Ultimate DIG GAME!!  ")
    print("---------------------------------------")
    print("---------------------------------------")
   
    print("")
    print("Enter")
    print("")
    print("Start for a new game")
    print("Rank to check the top 10")
    print("Exit to close the game")
    print("")
    user_action = input()
    
        
    if user_action == "Start":
        print("")
        print("   Enter player name:")
        user = input()
        game(user)
            
    elif user_action == "Rank":
        display_top_10()
        pass
    
    elif user_action == "Exit":
        break
        
    
    