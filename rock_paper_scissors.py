


while True:
    import random
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    user_choice = input("Rock, Paper, or Scissors? If you would not like to play, type exit. ")
    win_text = f"You win! The computer selected {computer_choice}."
    lose_text = f"You lose! The computer selected {computer_choice}. Try again"
    tie_text = f"It was a tie! The computer selected {computer_choice}. Try again!"


    #if user selects rock
    if user_choice.lower() == "rock" and computer_choice.lower() == "scissors":
        print(win_text)
        break
    if user_choice.lower() == "rock" and computer_choice.lower() == "paper":
        print (lose_text)
        continue
    if user_choice.lower() == "rock" and computer_choice.lower() == "rock":
        print(tie_text)
        continue
    
    #if user selects paper
    if user_choice.lower() == "paper" and computer_choice.lower() == "rock":
        print(win_text)
        break
    if user_choice.lower() == "paper" and computer_choice.lower() == "scissors":
        print (lose_text)
        continue
    if user_choice.lower() == "paper" and computer_choice.lower() == "paper":
        print(tie_text)
        continue

    #if user selects scissors
    if user_choice.lower() == "scissors" and computer_choice.lower() == "paper":
        print(win_text)  
        break
    if user_choice.lower() == "scissors" and computer_choice.lower() == "rock":
        print (lose_text)
        continue
    if user_choice.lower() == "scissors" and computer_choice.lower() == "scissors":
        print(tie_text)
        continue
    
    #if user wants to exit game
    if user_choice.lower() == 'exit':
        print("Thanks for playing!")
        break
    #if user types something incorrect
    else:
        print("Please select Rock, Paper, or Scissors.  If you pick anything else go play another game. ")
        continue