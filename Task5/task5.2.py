nums = []

for i in range(1000):
    user_input = input("Enter a number: ")

    if user_input == "":
        print("Goodbye")
        break

    nums.append(int(user_input))

nums.sort(reverse=True)

print("The five Greatest numbers are:")
for num in nums[:5]:
    print(num)


