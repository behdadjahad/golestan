from django.db import models
from golestan.users.models import BaseUser

from golestan.faculty.models import Faculty
from golestan.faculty.models import Major
from golestan.faculty.models import ApprovedCourse


# Create your models here.
class Professor(BaseUser) :
    class Meta :
        verbose_name_plural = 'Professor'
    
    faculty = models.ForeignKey(Faculty, on_delete=models.PROTECT)
    major = models.CharField(max_length=100)
    expertise = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    # presented_courses = models.ManyToManyField(ApprovedCourse.objects.filter(faculty=faculty), blank=True)
    
    @property   
    def presented_courses(self) :
        return self.termcourse_set.all()
    
    # def update_presented_courses(self, term_name) :
    #     pass
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def save(self, *args, **kwargs):
        self.set_password(self.password)
        super().save(*args, **kwargs)
    
    
    
    
class ITManager(BaseUser) :
    class Meta :
        verbose_name_plural = 'ITManager'
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        self.set_password(self.password)
        super().save(*args, **kwargs)


class EducationalAssistant(BaseUser) :
    class Meta :
        verbose_name_plural = 'EducationalAssistant'
    
    faculty = models.ForeignKey(Faculty, on_delete=models.PROTECT)
    major = models.ManyToManyField(Major)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        self.set_password(self.password)
        super().save(*args, **kwargs)


class Student(BaseUser) :
    class Meta :
        verbose_name_plural = 'Student'
    
    
    MILITARY_SERVICE_STATUS_CHOICES = (
        ('exempt', 'Exempt'),
        ('cardservice', 'CardService'),
        ('educationalexempt', 'EducationalExempt'),
    )

    entrance_year = models.DateField(auto_now_add=True)
    entrance_term = models.CharField(max_length=255)
    faculty = models.ForeignKey(Faculty, on_delete=models.PROTECT)
    major = models.ForeignKey(Major, on_delete=models.PROTECT)
    # courses = models.ManyToManyField('term.CourseStudent', related_name='enrolled_students', null=True, blank=True) # editted
    # courses = models.ManyToManyField(ApprovedCourse, through='term.CourseStudent', related_name='enrolled_students')
    years = models.PositiveIntegerField(default=0) # should be updated based on student requests
    supervisor = models.ForeignKey(Professor, on_delete=models.PROTECT, null=True, blank=True) 
    military_service_status = models.CharField(max_length=20, choices=MILITARY_SERVICE_STATUS_CHOICES)
    
    def save(self, *args, **kwargs):
        self.set_password(self.password)
        super().save(*args, **kwargs)
        
    @property   
    def passed_courses(self) :
        return self.courses.filter(course_status='passed')
    
    @property   
    def active_courses(self) :
        return self.courses.filter(course_status='active') 
    
    @property   
    def gpa(self) :
        passed_courses = self.passed_courses.all()
        totall_score = 0
        totall_units = 0
        if passed_courses.exists() :
            for course in passed_courses :
                score = course.student_score
                units = course.course.name.units
                totall_score += (score * units)
                totall_units += units
            if totall_units > 0 :
                return totall_score / totall_units
            
        else :
            return 0.0
        
    
    def term_score(self, term_name) :
        passed_courses = term_name.coursestudent_set.filter(student=self).filter(term_taken=term_name).filter(course_status='passed')
        totall_score = 0
        totall_units = 0
        if passed_courses.exists() :
            for coursestu in passed_courses :
                score = coursestu.student_score
                units = coursestu.course.units
                totall_score += (score * units)
                totall_units += units
            if totall_units > 0 :
                return totall_score / totall_units
            
        else :
            return 0.0

    

    # @property   
    # def years(self) :
    #     passed_courses = self.passed_courses.all()
    #     terms = []
    #     for course in passed_courses :
    #         term = course.coursestudent_set.filter(student=self).first().term_taken.term_name
    #         if term not in terms :
    #             terms.append(term)  
    #     return len(terms)
    
    
    # def add_to_passed_courses(self, course):
    #     CourseStudent.objects.create(student=self, course=course, course_status='passed')

    # def remove_from_passed_courses(self, course):
    #     CourseStudent.objects.filter(student=self, course=course, course_status='passed').delete()

    # def add_to_active_courses(self, course):
    #     CourseStudent.objects.create(student=self, course=course, course_status='active')

    # def remove_from_active_courses(self, course):
    #     CourseStudent.objects.filter(student=self, course=course, course_status='active').delete()
    
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    

        

        

