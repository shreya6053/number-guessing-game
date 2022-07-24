# Program to generate a random number between 0 and 50

# importing the random module
import random



randomVariable= (random.randint(0,50))
print(randomVariable)
score=100
hint = 1 
userInput=int(input("enter your guess "))
if (int(userInput )==  int(randomVariable)):
    print(" You have guessed correctly ")  

while (int(userInput)  != int(randomVariable)):
    

        score = score -10 
        if (score <= 0 ):
            print(str("You have lost"))
            break
        print("Your current score is ",str(score))
        if( hint == 1):
            if (randomVariable >= 0 and randomVariable <=10):
                print(str(" Hint This number lie between 0 and 10 "))
                hint = hint + 1

            elif(randomVariable >= 11 and randomVariable <= 20):
                print(str(" Hint This number lie between 11 and 20 "))
                hint = hint + 1

            elif(randomVariable >= 21 and randomVariable <= 30):
                print(str(" Hint This number lie between 21 and 30  "))
                hint = hint + 1

            elif (randomVariable >= 31 and randomVariable <= 40):
                print(str(" Hint This number lie between 31 and 40  "))
                hint = hint + 1

               
            elif (randomVariable >= 41 and randomVariable <= 50):
                print(str(" Hint This number lie between 41 and 50  "))
                hint = hint + 1

        elif(hint == 2):
            if (randomVariable >= 0 and randomVariable <= 5):
                print((" Hint This number lie between 0 and 5"))
                hint = hint + 1 

            elif ( randomVariable >=6 and randomVariable <= 10):
                print(str(" Hint This number lie between 6 and 10 "))
                hint = hint + 1 

         
            elif (randomVariable >= 11 and randomVariable <= 15):
                print(str(" Hint This number lie between 11 and 15"))
                hint = hint + 1 

            elif ( randomVariable >=16 and randomVariable <= 20):
                print(str(" Hint This number lie between 16 and 20 "))
                hint = hint + 1 
            
            
            elif (randomVariable >= 21 and randomVariable <= 25):
                print(str(" Hint This number lie between 21 and 25"))
                hint = hint + 1 

            elif ( randomVariable >=26 and randomVariable <= 30):
                print(str(" Hint This number lie between 26 and 30 "))
                hint = hint + 1 

            elif ( randomVariable >=31 and randomVariable <= 35):
                print(str(" Hint This number lie between 30 and 35 "))
                hint = hint + 1 
           
            elif ( randomVariable >=36 and randomVariable <= 40):
                print(str(" Hint This number lie between 36 and 40 "))
                hint = hint + 1 

            
            elif ( randomVariable >=41 and randomVariable <= 45):
                print(str(" Hint This number lie between 36 and 40 "))
                hint = hint + 1

            else:
                print(str(" Hint This number lie between 36 and 40 "))
                hint = hint + 1 
        elif(hint == 3):
            if (randomVariable % 2 == 0):
                print(str(" Hint This number is even"))
                hint = hint + 1 

            else :
                print(str( " hint the number is odd"))
 
  
   
        userInput=int(input(("enter your guess ")))
        if (int(userInput )==  int(randomVariable)):
            print(" You have guessed correctly ")   