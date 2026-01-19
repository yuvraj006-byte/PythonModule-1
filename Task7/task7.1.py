seasons = ["winter", "spring", "summer", "autumn"]

months = int(input("Enter the number a month (1,12): "))

if 1 <= months <= 12:
    season = seasons[(months % 12) // 3]
    print(season)
else:
    print("Please enter a valid month")