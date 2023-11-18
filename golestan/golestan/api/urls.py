from django.urls import path, include

urlpatterns = [
    path('admin/', include(('golestan.account.urls', 'student')))
]
