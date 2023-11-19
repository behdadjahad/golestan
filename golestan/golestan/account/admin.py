from django.contrib import admin

from golestan.account.models import Student, Professor, ITManager, EducationalAssistant

admin.site.register(Professor)
admin.site.register(ITManager)
admin.site.register(EducationalAssistant)
admin.site.register(Student)
