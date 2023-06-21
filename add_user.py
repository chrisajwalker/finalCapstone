def reg_user(user):
   
    while True:
        new_username = input("New Username: ")
        eligible_username = user.get(new_username, None)
        if eligible_username != None:
            print("Username already exists! Please choose a different user name")
            continue
        else:
            break
    new_password = input("New Password: ")
    confirm_password = input("Confirm Password: ")

    # check new password and password confirmation match before saving user
    if new_password == confirm_password:
        print("New user added")
        user[new_username] = new_password
        with open("user.txt", "w") as out_file:
            user_data = []
            for k in user:
                user_data.append(f"{k};{user[k]}")
            out_file.write("\n".join(user_data))
    else:
        print("Passwords do not match")