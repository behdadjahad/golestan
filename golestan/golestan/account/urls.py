from django.urls import path, include
from golestan.account.apis.students import StudentApi, StudentDetailApi
from golestan.account.apis.terms import TermsApi, TermDetailApi

urlpatterns = [
    path('students/', StudentApi.as_view(), name="students"),
    path('student/<int:id>/', StudentDetailApi.as_view(), name="student"),
    path('terms/', TermsApi.as_view(), name="terms"),
    path('term/<int:id>', TermDetailApi.as_view(), name="term"),

]
