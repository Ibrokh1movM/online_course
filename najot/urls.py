from django.urls import path
from .views import calendar_view, students_view

app_name = 'najot'

urlpatterns = [
    path('calendar/', calendar_view, name='calendar'),
    path('students/', students_view, name='students'),
]
