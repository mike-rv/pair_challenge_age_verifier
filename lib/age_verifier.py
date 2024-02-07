from datetime import datetime

def age_verifier(dateofbirth= None):
    if dateofbirth == None:
        raise Exception("Wrong date format!")
    
    user_dob_object = datetime.strptime(dateofbirth, "%Y-%m-%d").date()
    
    current_date = datetime.now().date()
    print(type(dateofbirth))
    age = current_date.year - user_dob_object.year - ((current_date.month, current_date.day) < (user_dob_object.month, user_dob_object.day))
    
    
    if age >= 16:
        return 'Access granted!'
    return 'Access denied!'



# print(age_verifier(''))