import saveproject
def searchProject():
    projectlists=saveproject.load_projects()
    found=False
    date=input("enter start date project : ")
    for proj in range(len(projectlists)):
        if projectlists[proj]["start_date"]==date:
            found=True
            print(projectlists[proj])
    if not found:
        print("Project not found🚫")

  