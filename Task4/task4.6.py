import random

points = int(input("Enter number of random points: "))
inside_circle = 0
total_points = 0

while total_points < points:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x*x + y*y < 1:
        inside_circle += 1

    total_points += 1

pi = 4 * inside_circle / total_points

print("Approximate value of pi:", pi)
