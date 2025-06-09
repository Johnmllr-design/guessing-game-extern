import random

# a python file for a random guessing game
guess = -1
rand = random.randint(1, 100)
i = 1
while guess != rand:
    if i > 10:
        print("Sorry, you've used all 10 attempts. The number was:", rand)
        break
    try:
        guess = int(input("Guess a number between 1 and 100: "))
        if guess < rand:
            print("Too low! Try again.")
        elif guess > rand:
            print("Too high! Try again.")
        else:
            print("Congratulations! You've guessed the number in " + str(i) + " attempts.")
    except ValueError:
        print("Please enter a valid integer.")
    i += 1


if __name__ == "__main__":  
    print("Game Over!")
    print("The random number was:", rand)
    print("Thanks for playing!")