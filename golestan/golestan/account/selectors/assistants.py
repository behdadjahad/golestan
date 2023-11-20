from django.db.models import QuerySet
from golestan.account.models import EducationalAssistant


def get_assistants() -> QuerySet[EducationalAssistant]:
    return EducationalAssistant.objects.all()

def get_assistant_detail(*, id:int) -> QuerySet[EducationalAssistant]:
    return EducationalAssistant.objects.get(id=id)