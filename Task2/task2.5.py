talents = float(input("Enter talents:"))
pounds = float(input("Enter pounds:"))
lots = float(input("Enter lots:"))

modernWeight = (talents * 20 * 32 * 13.3 + pounds * 32 * 13.3 + lots * 13.3)/1000

print("The weight in modern units:", modernWeight, "kilograms" )

