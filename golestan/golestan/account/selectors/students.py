from django.db.models import QuerySet
from golestan.account.models import Student


def get_students() -> QuerySet[Student]:
    return Student.objects.all()
