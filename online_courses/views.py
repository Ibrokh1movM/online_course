from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Teacher, Registration
from .forms import CourseForm
from django.core.mail import EmailMessage
from django.conf import settings
from .forms import RegistrationForm


# Create your views here.
def index(request):
    courses = Course.objects.all()
    teachers = Teacher.objects.all()
    context = {
        'courses': courses,
        'teachers': teachers
    }
    return render(request, 'online_courses/index.html', context)


from django.shortcuts import render
from django.core.mail import EmailMessage
from .forms import RegistrationForm


def register(request):
    success_message = None
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save()
            subject = "Kursga ro'yxatdan o'tdingiz!"
            message = f"Salom {registration.name},\n\nSiz {registration.course.title} kursiga muvaffaqiyatli ro'yxatdan o'tdingiz! Tez orada siz bilan bog'lanamiz.\n\nHurmat bilan,\nJamoamiz"
            sender_email = "muzaffaribrohimov7777@gmail.com"
            recipient_email = [registration.email]
            email = EmailMessage(subject, message, sender_email, recipient_email)
            email.send()
            success_message = "Siz muvaffaqiyatli ro‘yxatdan o‘tdingiz! Emailingizni tekshiring."
    else:
        form = RegistrationForm()

    return render(request, "online_courses/index.html", {"form": form, "success_message": success_message})


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
