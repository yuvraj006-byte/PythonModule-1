gender = input("Please type your gender: ")

hemoglobin = float(input("What is your Hemoglobin value(g/l): "))

if gender.lower().startswith("male"):
    if hemoglobin in range(134, 167):
        print("Your Hemoglobin is NORMAL")
    elif hemoglobin < 134:
        print("Your Hemoglobin is LOW")
    elif hemoglobin > 167:
        print("Your Hemoglobin is HIGH")
    else:
        print("Invalid Input.")

elif gender.lower().startswith("female"):
    if hemoglobin in range(117, 155):
        print("Your Hemoglobin is NORMAL")
    elif hemoglobin < 117:
        print("Your Hemoglobin is LOW")
    elif hemoglobin > 155:
        print("Your Hemoglobin is HIGH")
    else:
        print("Invalid Input.")

else:
    print("This Gender is not recognized.")