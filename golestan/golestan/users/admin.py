from django.contrib import admin
from golestan.account.models import Student, Professor, ITManager, EducationalAssistant

admin.site.register(Professor)
admin.site.register(ITManager)
admin.site.register(EducationalAssistant)

class CourseInline(admin.TabularInline):  # or admin.StackedInline
    model = Student.courses.through
    
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    inlines = [CourseInline]
