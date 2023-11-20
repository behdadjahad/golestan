from django.db.models import QuerySet
from golestan.account.models import Professor


def get_professors() -> QuerySet[Professor]:
    return Professor.objects.all()

def get_professor_detail(*, id:int) -> QuerySet[Professor]:
    return Professor.objects.get(id=id)