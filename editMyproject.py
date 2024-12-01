import validate
import saveproject
def editProject(projects):
    #projects=saveproject.load_projects()
    found=False
    Title = input("Enter Title project: ")
    if  validate.check_name(Title)==True :  
        for i in range(len(projects)):
            if projects[i]["Title"]==Title:
                found=True
                print('''if you want to update title press t | press d to update details 
                        |enter tar to update target|sd to update start date
                        | ed to update end date\n''')
                press=input("enter t|d|sd|ed|tar : ")
                if press=='d'.lower():
                    updateDetail=input("enter updated datail : ")
                    if validate.check_description(updateDetail):
                        projects[i]["Detail"]=updateDetail
                elif press=='tar'.lower():
                    updateTarget=input("enter updated target: ")
                    if validate.check_target(updateTarget):
                        projects[i]["target"]=updateTarget
                elif press=='sd'.lower():
                    updatestart_date=input("enter updated start_date : ")
                    if validate.check_date(updatestart_date):
                        projects[i]["start_date"]=updatestart_date
                elif press=='ed'.lower():
                    updateEnd_date=input("enter updated End_date :")
                    if validate.check_date(updateEnd_date):
                        projects[i]["end_date"]=updateEnd_date 
                elif press=='t'.lower():
                    updateTitle=input("enter updated Title L ")
                    if validate.check_name(updateTitle):
                        projects[i]["Title"]=updateTitle   

                                                   
    if not found:
        print(f'project {Title}not found')
        return projects