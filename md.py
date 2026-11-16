# from module import name as name1

# name="das"
# print(name)
# print(name1)

# import module
# print(module.fact(5))
# print(module.add(5,6))
# print(module.name)

# from module import name as name1,fact

# name="das" 
# print(name1)
# print(name)

# print(fact(9))

# import random
# print(random.randint(1,10))
# fruits=["Apple","Pineapple","Orange","Mango"]
# print(random.choice(fruits))


# import math 
# print(math.ceil(8.79))

#coin toss
# toss=["Head","Tail"]
# import random
# print("The toss is=",random.choice(toss))

#rock paper scissor game

import random
ch=["rock","scissor","paper"]
computer=random.choice(ch)
player="" 
while player not in ch:
    player=input("Enter your choice  /rock/Scissor/paper:").lower()
print(f"Commputer chose {computer}")
print(f"Player chose {player}")
if player==computer:
        print("Draw!!!")
elif player=="rock":
        if computer=="scissor":
            print("Player wins,rock beats scissor")
        else:
            print("Computer wins,paper covers rock")
elif player=="scissor":
        if computer=="rock":
            print("Computer wins,rock beats scissor")
        else:
            print("Player wins,scissor cuts paper")
elif player=="paper":
        if computer=="scissor":
            print("computer wins,scissor cuuts paper")
        else:
            print("player wins,paper covers rock")

