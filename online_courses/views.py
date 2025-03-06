from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Teacher
from .forms import CourseForm



# Create your views here.
def index(request):
    courses = Course.objects.all()
    teachers = Teacher.objects.all()
    context = {
        'courses': courses,
        'teachers': teachers
    }
    return render(request, 'online_courses/index.html', context)

def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'online_courses/course_detail.html', {'course': course})

def teacher_detail(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    return render(request, 'online_courses/teacher_detail.html', {'teacher': teacher})

def about(request):
    return render(request, 'online_courses/about.html')

def course(request):
    courses = Course.objects.all()
    context = {
        'courses': courses
    }
    return render(request, 'online_courses/course.html', context)

def teacher(request):
    teachers = Teacher.objects.all()
    context = {
        'teachers': teachers
    }
    return render(request, 'online_courses/teacher.html', context)

def contact(request):
    return render(request, 'online_courses/contact.html')

def blog(request):
    return render(request, 'online_courses/blog.html')

def detail(request):
    return render(request, 'online_courses/single.html')