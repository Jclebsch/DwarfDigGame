import random

# Items tuple, each index corresponds to an item
items = {
    "Stone": 0,  
    "Coal": 1,   
    "Cooper": 2,   
    "Iron": 2,     
    "Silver": 5,   
    "Gold": 10,     
    "Diamond": 100,  
    "Crystal": 1,  
    "Silmaril": 10000, 
    "Mithril": 10000,  
    "Gandalf": 0,  
    "Balrog": 10000   
}

# Probabilities for each item
probabilities = [
    (0, 0.2),   #STONE
    (0.2, 0.4), #COAL
    (0.4, 0.5), 
    (0.5, 0.60), 
    (0.60, 0.70), 
    (0.70, 0.75), 
    (0.75, 0.80), 
    (0.80, 0.88), 
    (0.88, 0.90), 
    (0.90, 0.92), 
    (0.92, 0.97), 
    (0.97, 1.00)  
]

user_action = ""  
score = 0          
miners_cart = {}   
rounds = 0         

def adjust_probability(base_probability):
    """Adjust probability with a random fluctuation of ±5%."""
    fluctuation = random.uniform(-0.05, 0.05)  
    return base_probability + fluctuation

def update_probabilities():
    """Increase the chance of finding Balrog if the player found Gandalf."""
    global probabilities
    
    if "Gandalf" in miners_cart:
        probabilities[11] = (probabilities[11][0], probabilities[11][0] + adjust_probability(0.10))  # Increase the chance of Balrog to 10%
    
    total_prob = sum([end - start for start, end in probabilities])
    probabilities = [(start / total_prob, end / total_prob) for start, end in probabilities]

def game():
    global user_action, rounds  

    print("Try to dig safely without going too deep.......\n")

    while True:
        random_number = random.random()
        global score
        
        if user_action.lower() == "yes" or user_action == "":
            print("Starting digging.......\n")
            
            update_probabilities()

            # Check which item corresponds to the random number
            for idx, (start, end) in enumerate(probabilities):
                if start <= random_number < end:
                    drawn_item = list(items.keys())[idx]
                    item_value = items[drawn_item]
                    number = idx + 1  
                    break

            print(f"You found: {drawn_item}")

            # If the item is Gandalf, check if it's already in the cart
            if drawn_item == "Gandalf":
                if "Gandalf" not in miners_cart:
                    print("\nGandalf the Grey is a strong ally!!\n")
                else:
                    print("\nYou already have Gandalf the Grey! Keep digging......\n")
            
            # If the number is 12 (Balrog), the user loses but if have Gandalf the game continues.
            if number == 12:
                if "Gandalf" in miners_cart:
                    print("\nGandalf the Grey is fighting the Balrog!!\nRUN YOU FOUL\n")
                    miners_cart.pop("Gandalf")
                else:
                    miners_cart.clear()
                    print("\nYou dig too deep.....")
                    print("---------------")
                    print("END OF THE GAME")
                    print("---------------")
                    print("FINAL SCORE")
                    print(f"{score}")
                    print("\nGoodbye!")
                    break

            # Add the found item to the player's cart
            if drawn_item in miners_cart:
                if drawn_item == "Gandalf" and "Gandalf" in miners_cart:
                    pass
                else:
                    miners_cart[drawn_item] += 1
            else:
                miners_cart[drawn_item] = 1

            # Check if the cart has more than 5 items
            if len(miners_cart) > 5:
                print("\nYour cart has more than 5 items!")
                print("Choose an item to remove:")

                # Display items in the cart with their quantities
                for item, quantity in miners_cart.items():
                    print(f"- {item} (x{quantity})")

                # Ask the user which item they want to remove
                item_to_remove = input("\nEnter the item you want to remove: ").strip().lower()

                # Check if the item exists in the cart
                item_found = False
                for item in miners_cart:
                    if item.lower() == item_to_remove:
                        miners_cart.pop(item)  # Remove the item from the cart
                        print(f"{item} has been removed from your cart.")
                        item_found = True
                        break

                if not item_found:
                    print(f"{item_to_remove} is not in your cart.")

                # Display updated cart
                print("\nItems in your cart after removal:")
                for item, quantity in miners_cart.items():
                    print(f"{item}: {quantity}")

            score += item_value
            
            print("\nItems in your cart:")
            for item, quantity in miners_cart.items():
                print(f"{item}, {quantity}")
            
            print("\nKeep digging? (YES or NO)\n")
            user_action = input().strip().upper()

            if user_action == "NO":
                miners_cart.clear()
                print(f"\nYou decided to stop the game. Your cart contains: {', '.join([f'{item}, {quantity}' for item, quantity in miners_cart.items()])}")
                print("\nFINAL SCORE")
                print(f"{score}")
                print("\nGoodbye!")
                break

        else:
            print("Invalid input! Please type 'YES' or 'NO'.\n")
            user_action = input("Do you want to start digging? (YES/NO): ").strip().upper()

# Start the game only when the script is executed directly
if __name__ == "__main__":
    game()
