from django.contrib import admin

from golestan.faculty.models import Faculty, Department, Major, ApprovedCourse


admin.site.register(Faculty)
admin.site.register(Department)
admin.site.register(Major)
admin.site.register(ApprovedCourse)