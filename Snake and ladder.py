
import random

# Snake and ladder game

Snake = {
    40: 3, 43: 18, 27: 5, 99: 41,
    95: 77, 89: 53, 66: 45, 54: 31
}

ladder = {
    4: 25, 13: 46, 42: 63,
    50: 69, 62: 81, 74: 92
}

player1 = input("Enter your name:")
player2 = input("Enter your name:")

pos1 = 0
pos2 = 0

while pos1 != 100 and pos2 != 100:

    dice1 = random.randint(1, 6)
    print("Number rolled for player 1 =", dice1)

    dice2 = random.randint(1, 6)
    print("Number rolled for player 2 =", dice2)

    # Player 1

    if pos1 == 0 and dice1 == 1:
        pos1 = 1
        print(player1, "enters the game at", pos1)

    elif pos1 > 0:
        if pos1 + dice1 <= 100:
            pos1 += dice1

            if pos1 in Snake:
                pos1 = Snake[pos1]
                print("Snake! New position =", pos1)

            elif pos1 in ladder:
                pos1 = ladder[pos1]
                print("Ladder! New position =", pos1)

            print("pos1 =", pos1)

    # Player 2

    if pos2 == 0 and dice2 == 1:
        pos2 = 1
        print(player2, "enters the game at", pos2)

    elif pos2 > 0:
        if pos2 + dice2 <= 100:
            pos2 += dice2

            if pos2 in Snake:
                pos2 = Snake[pos2]
                print("Snake! New position =", pos2)

            elif pos2 in ladder:
                pos2 = ladder[pos2]
                print("Ladder! New position =", pos2)

            print("pos2 =", pos2)

    if pos1 == 100:
        break

    if pos2 == 100:
        break

if pos1 == 100:
    print(player1, "wins")

elif pos2 == 100:
    print(player2, "wins")
