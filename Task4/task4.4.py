import random

random_int = random.randint(1, 10)

while True:
    user_input = int(input("Guess the number: "))

    if user_input > random_int:
        print("You guessed too high!")
    elif user_input < random_int:
        print("You guessed too low!")
    else:
        print("You guessed correctly!")
        break