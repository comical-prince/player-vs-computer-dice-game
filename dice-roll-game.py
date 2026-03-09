import random as r

while True:
    round = 1
    player_point = 0 
    computer_point = 0
    while round <= 5:
        print(f"Round {round}")
        player = r.randint(1,6)
        print(f"Player rolled : {player}")
        computer = r.randint(1,6)
        print(f"Computer rolled : {computer}")
        if player > computer :
            print("Player wins the round")
            player_point += 1
        elif player < computer :
            print("Computer wins the round")
            computer_point += 1
        else:
            print("It's a Draw")

        print()
        print("-"*30)
        round += 1 


    print("RESULT : ",end="")
    if player_point > computer_point:
        print("Player wins the Game")
    elif player_point < computer_point:
        print("Computer wins the Game")
    else:
        print("It's a draw")

    choice = input("Do u want to play again?(Y/N) : ").lower()
    if choice != "y":
        print("Thanks for playing")
        break