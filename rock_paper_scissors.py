import random 

rock_art = """
    __________
---'       ____)
         (______)     
         (______)
         (_____)
---.____ (____)
       
       """

paper_art = """   
    _______
---'   ____)___
         ______)
         ______)  
       _______)
---.________)
"""

scissors_art = """
    ________
---'    ____)____
          _______)
        _________)
        (_____)
---.____(____)                   
        
      """
        
ascii_art = {"rock": rock_art, "paper": paper_art, "scissors": scissors_art}  


print("Welcome to Rock, Paper, Scissors Game!")
print("Type 'rock', 'paper', or 'scissors' to play.\nType 'quit' to exit the game.")

choices = ["rock", "paper", "scissors"]
player_score = 0
computer_score = 0

while True:
    player_choice = input("Your choice: ").lower()
    
    if player_choice == "quit":
        print("Thanks for playing! Final Scores:")  
        print(f"Player: {player_score}\nComputer: {computer_score}")
        break

    if player_choice not in choices:
        print("Invalid choice. Please try again.")
        continue

    computer_choice = random.choice(choices)
    

    print(f"Your choice is {player_choice}")
    print(ascii_art[player_choice])

    print(f"Computer's choice is {computer_choice}")
    print(ascii_art[computer_choice])
    
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

        