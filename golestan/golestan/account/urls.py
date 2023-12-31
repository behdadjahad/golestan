from django.urls import path, include
from golestan.account.apis.students import StudentApi, StudentDetailApi
from golestan.account.apis.terms import TermsApi, TermDetailApi
from golestan.account.apis.faculties import FacultyApi, FacultyDetailApi
from golestan.account.apis.assistants import AssistantApi, AsistantDetailApi
from golestan.account.apis.professors import ProfessorApi, ProfessorDetailApi

urlpatterns = [
    path('students/', StudentApi.as_view(), name="students"),
    path('student/<int:id>/', StudentDetailApi.as_view(), name="student"),
    path('terms/', TermsApi.as_view(), name="terms"),
    path('term/<int:id>', TermDetailApi.as_view(), name="term"),
    path('faculties/', FacultyApi.as_view(), name="faculties"),
    path('faculty/<int:id>', FacultyDetailApi.as_view(), name="faculty"),
    path('assistants/', AssistantApi.as_view(), name="assistants"),
    path('assistant/<int:id>', AsistantDetailApi.as_view(), name="assistant"),
    path('professors/', ProfessorApi.as_view(), name="professors"),
    path('professor/<int:id>', ProfessorDetailApi.as_view(), name="professor"),
]
