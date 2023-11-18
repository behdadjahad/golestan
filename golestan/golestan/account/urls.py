from django.urls import path, include
from golestan.account.apis.students import StudentApiForItManager

urlpatterns = [
    path('student/', StudentApiForItManager.as_view(),name="student")
]
