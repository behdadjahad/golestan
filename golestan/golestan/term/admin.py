from django.contrib import admin

from golestan.term.models import Term, TermCourse, CourseStudent, RegistrationRequest

admin.site.register(Term)
admin.site.register(TermCourse)
admin.site.register(CourseStudent)
admin.site.register(RegistrationRequest)