
import validate

class CreateProject:
    def __init__(self):
            
            while True:
                Title = input("Enter Title project: ")
                if  validate.check_name(Title)==False:  
                    print("Invalid title") 
                else:
                    self.Title = Title 
                    break  
            
                
            while True:
                Detail= input("Enter project description: ")
                if  validate.check_description(Detail)==False:  
                    print("Invalid description") 
                else:
                    self.Detail= Detail  
                    break 
            while True: 
                target=input("enter total target: ")
                if  not validate.check_target(target):
                    print("invalid target: ")
                else:
                    self.target=target
                    break

            while True: 
                start_date=input("enter start date project: ")
                if  validate.check_date(start_date):
                    print("invalid date: ")
                else:
                    self.start_date=start_date
                    break
            while True: 
                end_date=input("enter end date project: ")
                if  validate.check_date(end_date) :
                       print("invalid date: ")
                elif not validate.compare_dates(self.start_date,end_date):
                     print("end date must be after start date")
                else:
                    self.end_date=end_date
                    break


            

            

