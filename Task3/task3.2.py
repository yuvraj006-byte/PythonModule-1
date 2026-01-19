cabin_class = input("Please enter the cabin class (LUX, A, B or C):")

if cabin_class.lower().startswith("lux"): print("It is an upper-deck cabin with a balcony.")
elif cabin_class.lower().startswith("a"): print("It is above the car deck, equipped with a window.")
elif cabin_class.lower().startswith("b"): print("It is a windowless cabin above the car deck.")
elif cabin_class.lower().startswith("c"): print("It is a windowless cabin below the car deck.")
else:
    print("Invalid cabin class!")