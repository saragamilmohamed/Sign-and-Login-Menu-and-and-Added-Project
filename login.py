import json

def login():
    user_ = json.load(open("users.json")) 
    
    while True:
        _email=input("Enter email: ")
        user_found=False 
        for user in user_:
            if _email==user["email"]:
                user_found=True
                _password=input("Enter your password: ")
                if _password==user["password"]:
                    print("Login successful ✅")
                    return True
                else:
                    print("Incorrect password,Please try again🤦‍♀️.")
                    break  
        if not user_found:
            print("Email not found.Please try again⛔.")

            
            