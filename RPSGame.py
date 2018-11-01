from random import randint

# available weapon => store this in an array
choices = ["Rock", "Paper", "Scissors"]

computer_live = 3
player_live = 3
player = False

# make the computer pick one item at random
computer = choices[randint(0, 2)]

# show the computer's choice in the terminal window
print("Computer chooses: ", computer)

while player is False:
    print("Chooses your weapon!\n")
    player = input("Rock, Paper or Scissors?\n")
    print("player chooses:", player)

    # check to see if you picked the same thing
    if (player == computer):
        print("Tie! Live to shoot another day")

    elif player == "Rock":
        if computer == "Paper":
            # computer won
            player_live = player_live - 1
            print("you lose! HP -1", computer, "covers", player)
        print("You live:", player_live, "com. life", computer_live, "come on!")
    else:
            print("you win! Computer HP -1", player, "smashes", computer)
    print("you live:", player_live, "com. live:", computer_live, "come on!")

    elif player_live == "Scissors":
            if computer == "Rock":
                Player_live = player_live - 1
                print("you lose! HP -1", computer, "smashesm", player)
    print("You life:", player_live, "Com. life:", computer_live, "Cheer up!")
    else:
                print("you win! Computer HP-1", player, "cuts", computer)
    print("You life:", player_live, "Com. life:", computer_live, "Keep on!")
    elif player == "Paper":
        if computer == "Scissors":
            player_live = player_live - 1
            # computer won
            print("You lose! HP -1", computer, "cuts", player)
    print("You life:", player_live, "Com. life:", computer_live, "Cheer up!")
    else:
            print("You win! Computer HP -1", player, "covers", computer)
    print("You life:", player_live, "Com. life:", computer_live, "Keep on!")
    elif player == "quit":
            exit()
    else:
        print("not a valid option. check again, and check ur spelling!\n")
        if player_live > 0 and computer_live > 0:
            player = False
        computer = choices[randint(0, 2)]
    else:
        if PlayerLife == 0:
            print("gameover, contiune?")
        else:
            print("congratulation! contiune?")
