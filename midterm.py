#Lauren Bowman
#Midterm Question 2

#mynumber
mynumber = 6

guessednumber = False

while not guessednumber:

    guess = int(input("Guess a number between 1 and 10. "))

    if guess == mynumber:
        print(" Yay you're right!")
        guessednumber = True
    elif guess < mynumber:
        print("Too low, try again.")
    elif guess > mynumber:
         print("Too high; try again.")

