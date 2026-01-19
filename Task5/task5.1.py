import random

dice = [1, 2, 3, 4, 5, 6]
num_dice = int(input("Enter the Numbers of dice to roll: "))

total = 0

for i in range(num_dice):
    roll = random.randint(1, 6)
    total += roll

print("The sum of all the rolls is: ", total)