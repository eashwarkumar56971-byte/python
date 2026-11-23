#Hangman out game
import random
movies=["Prestige","Odyssey","Memento","Dark Knight","Dunkirk","Following","Inception","Interstellar"]
movie=random.choice(movies)
display=""
count=0



guessed=[]
for i in movie:

    if i==" ":
        display+="  "
    else:
        display+=" _ "
print(display)

letter_attempts=6
movie_attempts=2
new_count=len(movie)





while letter_attempts!=0 and movie_attempts!=0 and new_count!=count:
  new_display=""
  count=0
  
  


  
  guess=input("Enter your guess:").lower()
  
  if guess in guessed:
     print("Don't repeat the letter")
     
     continue
  elif len(guess)==1 and guess in movie.lower():
     guessed.append(guess)
     
    

  if len(guess)>1:
    if guess==movie.lower():
        print("You have won!!!")
        print(f"The movie is {movie}")
        break
    else:
        print("You are wrong")
        movie_attempts-=1
        print("Remaining movie attempts=",movie_attempts)
       
        if movie_attempts==0:
           print("Game over")
           print(f"Answer={movie}")
           break
           
  elif len(guess)==1:
    if guess in movie.lower():
        print('You have guessed correct')
        
        

    else:
        print("wrong guess")
        letter_attempts-=1
        print("Remaining letter attempts=",letter_attempts)
        if letter_attempts==0:
           print("Game over")
           print(f"Answer={movie}")
           break
  
  
  for i in movie:
     if i==" ":
        new_display+=" "
     elif i.lower() in guessed and len(i)==1:
        new_display+=i+" "
        
     elif i.lower() in guess and len(guess)==1:
       new_display+=guess
     else:
        new_display+=" _ "
  print(new_display)

  for i in movie.lower():
     if i in guessed:
        count+=1
        
     if count==len(movie):
        print("You won!!!")
        print(f"The movie is={movie}")
        new_count=count
        break
        
      
      
     
     

  
    



    
