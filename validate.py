import re
from datetime import datetime

def check_email(email):
    return re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email)

def check_phone(phone):
    return re.match(r"^01[0-2|5]\d{8}$", phone)

def check_name(fname):
    if fname.isdigit() or fname.strip()=="" or len(fname)==0:
        return False
    return True
def check_date(date, date_format="%Y-%m-%d"):
    try:
        datetime.strptime(date, date_format)
        return True
    except ValueError:
        return False

def check_description(desc):
    if desc.isdigit() or desc.strip()=="" or len(desc)<10:
        return False
    return True
def check_target(target):
    if not target.isdigit() :
        return False
    return True



def compare_dates(date1, date2, date_format="%d/%m/%Y"):

    date1 = datetime.strptime(date1, date_format).date()
    date2 = datetime.strptime(date2, date_format).date()
    
    if date1 < date2:
        return True
    else:
        return False

