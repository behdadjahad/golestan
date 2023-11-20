from django.db.models import QuerySet
from golestan.term.models import Term


def create_term(*,
                term_name:str,
                unit_selection_start_time,
                unit_selection_end_time,
                courses_start_time,
                courses_end_time,
                repairing_unit_selection_start_time,
                repairing_unit_selection_end_time,
                emergency_deletion_start_time,
                emergency_deletion_end_time,
                exams_start_time,
                term_end_time)-> QuerySet[Term]:
    
    return Term.objects.create(
        term_name=term_name,
        unit_selection_start_time=unit_selection_start_time,
        unit_selection_end_time=unit_selection_end_time,
        courses_start_time=courses_start_time,
        courses_end_time=courses_end_time,
        repairing_unit_selection_start_time=repairing_unit_selection_start_time,
        repairing_unit_selection_end_time=repairing_unit_selection_end_time,
        emergency_deletion_start_time=emergency_deletion_start_time,
        emergency_deletion_end_time=emergency_deletion_end_time,
        exams_start_time=exams_start_time,
        term_end_time=term_end_time)


def update_term() -> QuerySet[Term]:
    pass

def delete_term(*, id:int) -> QuerySet[Term]:
    
    term = Term.objects.get(id=id)
    if term is None:
        raise Exception("There is no student with this id.")
    
    term.delete()
        
