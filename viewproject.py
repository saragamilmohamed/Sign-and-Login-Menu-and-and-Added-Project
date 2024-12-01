
import saveproject
def viewProject():
     projectlists=saveproject.load_projects()
     for i in projectlists:
          print(i)

