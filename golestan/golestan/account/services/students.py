from django.db.models import QuerySet
from golestan.account.models import Student
from golestan.faculty.models import Faculty
from golestan.faculty.models import Major


def create_student(*,
                   first_name:str,
                   last_name:str,
                   account_number:str,
                   phone_number:str,
                   national_id:str,
                   birth_date,
                   gender:str,
                   military_service_status:str,
                   entrance_year,
                   entrance_term:str,
                   email:str,
                   password:str,
                   faculty:int,
                   major:int
                   )-> QuerySet[Student]:
    

    major_object = Major.objects.get(id=major)
    if  major_object is None:
        raise Exception("There is no major with this id.")

    faculty_object = Faculty.objects.get(id=faculty)
    if faculty_object is None:
        raise Exception("There is no faculty with this id.")
    

    return Student.objects.create(
        first_name=first_name,
        last_name=last_name,
        phone_number=phone_number,
        account_number=account_number,
        national_id=national_id,
        birth_date=birth_date,
        gender=gender,
        military_service_status=military_service_status,
        entrance_year=entrance_year,
        entrance_term=entrance_term,
        email=email,
        password=password,
        faculty=faculty_object,
        major=major_object)


def update_student() -> QuerySet[Student]:
    pass

def delete_student(*, id:int) -> QuerySet[Student]:
    
    student = Student.objects.get(id=id)
    if student is None:
        raise Exception("There is no student with this id.")
    
    student.delete()
        
