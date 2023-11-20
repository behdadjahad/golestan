from django.db.models import QuerySet
from golestan.faculty.models import Faculty


def create_faculty(*, name:str)-> QuerySet[Faculty]:
    
    return Faculty.objects.create(name=name)


def update_faculty() -> QuerySet[Faculty]:
    pass

def delete_faculty(*, id:int) -> QuerySet[Faculty]:
    
    faculty = Faculty.objects.get(id=id)
    if faculty is None:
        raise Exception("There is no faculty with this id.")
    
    faculty.delete()
        