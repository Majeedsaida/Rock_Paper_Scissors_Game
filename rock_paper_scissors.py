print("Welcome to Rock, Paper, Scissors Game!")
print("Type 'rock', 'paper', or 'scissors' to play.\nType 'quit' to exit the game.")

choices = ["rock", "paper", "scissors"]
player_score = 0
computer_score = 0
round_count = 0

while True:
    player_choice = input("Your choice: ").lower()
    
    if player_choice == "quit":
        print("Final Scores:")  
        print(f"Player: {player_score}\nComputer: {computer_score}")
        break

    if player_choice not in choices:
        print("Invalid choice. Please try again.")
        continue

    computer_choice = choices[round_count]
    round_count += 1

   
    if round_count == len(choices):
        round_count = 0

    
    print(f"Computer's choice is {computer_choice}")

    
    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"):
        print("You win this round!") 
        player_score += 1
    else: 
        print("Computer wins this round!")
        computer_score += 1