import os
import json

# Directory where the JSON file will be saved
directory = "data"
os.makedirs(directory, exist_ok=True)  # Creates the 'data' folder if it doesn't exist

# Full path to the JSON file
user_rank_json = os.path.join(directory, "user_rank.json")

def save_rank(player, final_score):
    rankings = []

    # Check if the JSON file exists before trying to load its data
    if os.path.exists(user_rank_json):  
        with open(user_rank_json, "r", encoding="utf-8") as files:
            try:
                rankings = json.load(files)  # Load existing data
            except json.JSONDecodeError:
                print("The JSON file is empty or corrupted. Creating a new one...")

    # Add the new player to the ranking
    rankings.append({
        "player": player,
        "score": final_score
    })

    # Save the updated data to the JSON file
    with open(user_rank_json, "w", encoding="utf-8") as files:
        json.dump(rankings, files, indent=4, ensure_ascii=False)

    print(f"Data for {player} successfully added to {user_rank_json}!")

def load_rankings():
    """Load the JSON file."""
    if os.path.exists(user_rank_json):
        with open(user_rank_json, "r", encoding="utf-8") as file:
            try:
                return json.load(file)  # Return the ranking data
            except json.JSONDecodeError:
                print("Error loading the JSON file. It is empty or corrupted.")
                return []
    else:
        return []  # Return an empty list if the file doesn't exist

def display_top_10():
    """Display the top 10 players."""
    rankings = load_rankings()

    if not rankings:
        print("The ranking is empty. Play a game to create it!")
        return

    # Sort the ranking by score (highest to lowest)
    sorted_rankings = sorted(rankings, key=lambda x: x["score"], reverse=True)

    print("\n----------- TOP 10 Players -----------")
    for idx, player in enumerate(sorted_rankings[:10], start=1):
        print(f"{idx}. {player['player']} - {player['score']} points")
    print("-------------------------------------\n")
