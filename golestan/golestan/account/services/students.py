from django.db.models import QuerySet
from golestan.account.models import Student


def create_student(first_name:str,
                   last_name:str,
                   account_number:str,
                   phone_number:str,
                   national_id:str,
                   birth_date,
                   gender:str,
                   militery_service_status:str,
                   intrance_year,
                   email:str
                   )-> QuerySet[Student]:
    
    return Student.objects.create(
        first_name=first_name,
        last_name=last_name,
        phone_number=phone_number,
        account_number=account_number,
        national_id=national_id,
        birth_date=birth_date,
        gender=gender,
        militery_service_status=militery_service_status,
        intrance_year=intrance_year,
        email=email)
