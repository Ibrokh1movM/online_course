from django.shortcuts import render, redirect
from .models import Data, Students

def calendar_view(request):
    return render(request, 'calendar.html')


def students_view(request):
    selected_date = request.GET.get('date')

    if not selected_date:
        return redirect('calendar')

    data, created = Data.objects.get_or_create(date=selected_date)

    all_students = Students.objects.values_list('fullname', flat=True).distinct()

    students = Students.objects.filter(data=data)

    for student_name in all_students:
        if not students.filter(fullname=student_name).exists():
            Students.objects.create(fullname=student_name, status='pending', data=data)

    students = Students.objects.filter(data=data)

    if request.method == "POST":
        for student in students:
            new_status = request.POST.get(f'status_{student.id}')
            if new_status and student.status != new_status:
                student.status = new_status
                student.save()

        return redirect(f'/students/?date={selected_date}')

    return render(request, 'students.html',
                  {'students': students, 'selected_date': selected_date, 'no_students': False})
