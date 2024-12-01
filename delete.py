import validate
import saveproject

def delProject(projects):
    found=False
    #projects = saveproject.load_projects()
    Title = input("Enter the Title of the project to delete: ")

    if validate.check_name(Title):
        for i in range(len(projects)):
           
            if projects[i]["Title"] == Title:
                found=True
                del projects[i]
                print(f"project {Title} deleted")
        
    if not found:
        print("Project not found🚫")
    return projects
        
