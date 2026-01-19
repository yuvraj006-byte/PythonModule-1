name_set = set()

while True:
    user_input = input("Please enter a Name: ")


    if user_input == "":
        print("These where the names you Typed!:", name_set)
        break

    if user_input in name_set:
        print("Existing Name")
    else:
        name_set.add(user_input)
        print("New Name")
