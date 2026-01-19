while True:
    inches = float(input("Enter inches: "))
    centimeters = inches * 2.54

    if inches < 0:
        print("Goodbye!")
        break

    print(centimeters, "cm")



