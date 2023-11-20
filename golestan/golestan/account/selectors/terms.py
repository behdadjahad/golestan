from django.db.models import QuerySet
from golestan.term.models import Term


def get_terms() -> QuerySet[Term]:
    return Term.objects.all()

def get_term_detail(*, id:int) -> QuerySet[Term]:
    return Term.objects.get(id=id)