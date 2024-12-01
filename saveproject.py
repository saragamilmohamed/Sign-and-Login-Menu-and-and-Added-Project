import json
projectlists=[]
Project_FILE = "projects.json"
def save_projects(project):
    with open(Project_FILE, "w") as file:
        json.dump(project, file, indent=4)
def load_projects():
    try:
        with open("projects.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return [] 