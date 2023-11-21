from django.urls import path, include

urlpatterns = [
    path('admin/', include(('golestan.account.urls', 'admin entities'))),
    # path("assistant", include('golestan.faculty.urls', 'assistant entities'))
]
