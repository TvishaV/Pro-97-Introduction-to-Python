import random

randomNumber = random.randint(1,9)

chances = 0


while (chances<5):
    guess = int(input("Enter the number you think is the answer between 1 to 9:"))

    if guess == randomNumber:
      print("Congratulations YOU WON!!!")
      break
    
    elif guess< randomNumber:
        print("Your guess was lower than the number generated")

    else:
        print("Your guess was higher than the number generated")   

    chances+= 1     

if chances > 5:
    print("YOU LOSE!!! The number is" , randomNumber)