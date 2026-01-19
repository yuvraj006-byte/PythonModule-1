correct_username = "python"
correct_password = "rules"

attempts = 0
max_attempts = 5

while True:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    attempts += 1
    if username == correct_username and password == correct_password:
        print("Welcome")
        break
    elif attempts == max_attempts:
        print("Access denied")
        break
    else:
        print("Wrong username or password")


