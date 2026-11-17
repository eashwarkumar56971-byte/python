#create a rpg game
import random
P1=100
P2=100

Player1=input("Enter the name of player1:")
Player2=input("Enter the name of player2:")


while P1 and P2>0:
    
    hp1=random.randint(0,20)
    hp2=random.randint(0,20)
    
    
    if hp1>P1:
        continue
    elif hp2>P2:
        continue

    Point1=P1-hp1
    Point2=P2-hp2
    print("Player 1 Attacks Player 2,Remaining Hp For player 2=",Point2)
    P2=Point2
    if P2==0:
         break
    
    print("Player 2 Attacks Player1,Remaining Hp for player 1=",Point1)
    P1=Point1

    if P1==0:
         break
    print(P1,P2)
    
         
if P1==0 or P2==0:
        if P1==0:
            print("Game over,Player 2 wins",Player2)
            
        elif P2==0:
            print("Game over,Player 1 wins",Player1)
         



