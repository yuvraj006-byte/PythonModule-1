nums = []
while True:
    user_input = input("Press Enter a Number: ")

    if user_input == "":
        print("Goodbye!")
        break

    nums.append(float(user_input))

print("The smallest number entered is " + str(min(nums)))
print("The largest number entered is " + str(max(nums)))
