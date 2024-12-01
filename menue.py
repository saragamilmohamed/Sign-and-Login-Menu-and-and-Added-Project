import registration
import login
import saveusers
import CreateProject
import saveproject
import viewproject
import projectSearch
import editMyproject
import delete
userlists = saveusers.load_users()
projectlists=saveproject.load_projects()
print("------------Welcome-------------")
print("create account if you don't have account in our site or login if you have account already")
register=input("enter yes to register or no to login if you have account already ")
if register=="yes"or register=="Yes"or register=='Y'or register=='y':
    user=registration.registraion()
    print("created account sucessfully 🤩")
    userlists.append(user.__dict__)
else:
    user_login=login.login()
    if user_login:
        print('''if you want to create project enter CP or view all project press v
            or s to search for specific project of e to edit your project
            or d to delete  your project''')
        enter=input("enter your choice:")
        if enter=="CP" or enter=='cp':
            project=CreateProject.CreateProject()
            projectlists.append(project.__dict__)
        elif  enter == 'v' or enter =='V':
            viewproject.viewProject()
        elif enter =='S' or enter=='s':
            projectSearch.searchProject()
        elif enter =='e'.lower():
            editMyproject.editProject(projectlists)
            
        elif enter =='d'.lower():
            delete.delProject(projectlists)
            


saveproject.save_projects(projectlists)
saveusers.save_users(userlists)  