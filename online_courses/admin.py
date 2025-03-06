from django.contrib import admin

from online_courses.models import Course, Teacher

# Register your models here.
admin.site.register(Course)
admin.site.register(Teacher)