str_user_name = input(str("Username: "))
str_password = input(str("Password: "))

user_name = "python"
password = "rules"

attempts = 0
max_attempts = 5

while attempts < max_attempts:
    if str_user_name == "python" and str_password == "rules":
     print("Welcome")
     break
    else:
     attempts += 1
     if attempts < max_attempts:
        print("Incorrect credentials, try again.")
        str_user_name = input("Username: ")
        str_password = input("Password: ")
if attempts == max_attempts:
    print("Access denied")