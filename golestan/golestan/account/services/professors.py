from django.db.models import QuerySet
from golestan.account.models import Professor
from golestan.faculty.models import Faculty
from golestan.faculty.models import Major

def create_professor(*,
                     first_name:str,
                     last_name:str,
                     account_number:str,
                     phone_number:str,
                     national_id:str,
                     birth_date,
                     gender:str,
                     email:str,
                     password:str,
                     faculty:int,
                     major:int,
                     expertise:str,
                     degree:str)-> QuerySet[Professor]:
    

    major_object = Major.objects.get(id=major)
    if  major_object is None:
        raise Exception("There is no major with this id.")

    faculty_object = Faculty.objects.get(id=faculty)
    if faculty_object is None:
        raise Exception("There is no faculty with this id.")
    

    return Professor.objects.create(
        first_name=first_name,
        last_name=last_name,
        phone_number=phone_number,
        account_number=account_number,
        national_id=national_id,
        birth_date=birth_date,
        gender=gender,
        email=email,
        password=password,
        faculty=faculty_object,
        major=major_object,
        expertise=expertise,
        degree=degree)


def update_professor() -> QuerySet[Professor]:
    pass

def delete_professor(*, id:int) -> QuerySet[Professor]:
    
    professor = Professor.objects.get(id=id)
    if professor is None:
        raise Exception("There is no prfessor with this id.")
    
    professor.delete()
        
