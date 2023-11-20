from django.db.models import QuerySet
from golestan.account.models import EducationalAssistant
from golestan.faculty.models import Faculty


def create_assistant(*,
                   first_name:str,
                   last_name:str,
                   account_number:str,
                   phone_number:str,
                   national_id:str,
                   birth_date,
                   gender:str,
                   email:str,
                   password:str,
                   faculty:int,)-> QuerySet[EducationalAssistant]:
    

    faculty_object = Faculty.objects.get(id=faculty)
    if faculty_object is None:
        raise Exception("There is no faculty with this id.")
    

    return EducationalAssistant.objects.create(
        first_name=first_name,
        last_name=last_name,
        phone_number=phone_number,
        account_number=account_number,
        national_id=national_id,
        birth_date=birth_date,
        gender=gender,
        email=email,
        password=password,
        faculty=faculty_object)


def update_assistant() -> QuerySet[EducationalAssistant]:
    pass

def delete_assistant(*, id:int) -> QuerySet[EducationalAssistant]:
    
    assistant = EducationalAssistant.objects.get(id=id)
    if assistant is None:
        raise Exception("There is no student with this id.")
    
    assistant.delete()
        
