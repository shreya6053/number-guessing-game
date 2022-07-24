# Program to generate a random number between 1 and 100

# importing the random module
import random



randomVariable= (random.randint(1,100))
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
            if (randomVariable % 2 == 0):
                print(str(" Hint this is an even number "))
                hint = hint + 1

            else :
                print(str("  Hint this is an odd number "))
                hint = hint + 1
        elif(hint == 2):
            if (randomVariable % 3 == 0):
                print(str(" Hint this is a multiple of 3  "))
                hint = hint + 1

            else :
                print(str("  Hint this is not a multiple of 3 "))
                hint = hint + 1

        elif(hint == 3):
            if (randomVariable % 5 == 0):
                print(str(" Hint this is a multiple of 5 "))
                hint = hint + 1

            else :
                print(str("  Hint this is not a multiple of 5 "))
                hint = hint + 1            
        elif(hint == 4):
            if (randomVariable % 7 == 0):
                print(str(" Hint this is a multiple of 7 "))
                hint = hint + 1

            else :
                print(str("  Hint this is not a multiple of 7 "))
                hint = hint + 1            

          

        userInput=int(input(str("enter your guess ")))
        if (int(userInput )==  int(randomVariable)):
            print(" You have guessed correctly ")   

    




    




