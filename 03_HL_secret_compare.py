# HL component 3 - compares user guess with secret number

SECRET = 7

guess = ""

while guess != SECRET:

    guess = int(input("Guess: "))  # replace this with a function

    if guess < SECRET:
        print("Too low, try a lower number")
    elif guess > SECRET:
        print("Too high, try a higher number")
    else:
        print("Well done! You guessed the secret number")


