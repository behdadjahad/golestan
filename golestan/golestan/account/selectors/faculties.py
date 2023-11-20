from django.db.models import QuerySet
from golestan.faculty.models import Faculty


def get_faculties() -> QuerySet[Faculty]:
    return Faculty.objects.all()

def get_faculty_detail(*, id:int) -> QuerySet[Faculty]:
    return Faculty.objects.get(id=id)