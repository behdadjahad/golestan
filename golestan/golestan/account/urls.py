from django.urls import path, include
from golestan.account.apis.students import StudentApi, StudentDetailApi

urlpatterns = [
    path('students/', StudentApi.as_view(), name="students"),
    path('student/<int:id>/', StudentDetailApi.as_view(), name="student")

]
