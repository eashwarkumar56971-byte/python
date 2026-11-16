#die game
import random
player_1=(random.randint(1,6))
print (player_1)
player_2=(random.randint(1,6))
print (player_2)
count1=0
count2=0
sum1=0
sum2=0

for i in range(1,(player_1)+1):
    count1=random.randint(1,6)
    print("count1=",count1)
    
    sum1+=count1

for j in range(1,(player_2)+1):
    count2=random.randint(1,6)
    
    print("count2=",count2)
    sum2+=count2


if sum1==sum2:
    print("draw")
elif sum1>sum2:
    print("Player 1 wins")
else:
    print("Player 2 wins")
print("sum1=",sum1)
print("sum2=",sum2)