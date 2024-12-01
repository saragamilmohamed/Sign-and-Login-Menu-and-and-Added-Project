
import validate

class registraion:
    def __init__(self):
            
            while True:
                fname = input("Enter your first name: ")
                if  validate.check_name(fname)==False:  
                    print("Invalid name") 
                else:
                    self.Fname = fname  
                    break  
            
                
            while True:
                lname = input("Enter your last name: ")
                if  validate.check_name(lname)==False:  
                    print("Invalid name") 
                else:
                    self.Lname = lname  
                    break 
            while True: 
                email=input("enter your email: ")
                if not validate.check_email(email):
                    print("Invalid Email: ")
                else:
                    self.email=email
                    break
            

            
            self.password=input("enter your password : ")

            self.comfirmed=input("confirm your password: ")
            while True:
                phone=input("enter your phone number :")
                if not validate.check_phone(phone):
                    print("Invalid phone number: ")
                    return
                else:
                    self.phone=phone
                    break


