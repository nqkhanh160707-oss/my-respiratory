correct_username = "python"
correct_password = "rules"

attempt = 0 

while attempt < 5:
        username = input("Enter username: ")
        password = input("Enter password: ")
        
        if username == correct_username and password == correct_password:
            print("Access granted.")
            break
        else:
            attempt += 1
            print(f"Access denied. You have {5 - attempt} attempts left.")