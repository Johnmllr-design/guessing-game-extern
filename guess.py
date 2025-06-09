import random

# a python file for a random guessing game
guess = -1
rand = random.randint(1, 100)
while guess != rand:
    try:
        guess = int(input("Guess a number between 1 and 100: "))
        if guess < rand:
            print("Too low! Try again.")
        elif guess > rand:
            print("Too high! Try again.")
        else:
            print("Congratulations! You've guessed the number!")
    except ValueError:
        print("Please enter a valid integer.")


if __name__ == "__main__":  
    print("Game Over!")
    print("The random number was:", rand)
    print("Thanks for playing!")