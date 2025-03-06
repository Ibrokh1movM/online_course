from django.urls import path
from online_courses import views

app_name = 'online_courses'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('course/', views.course, name='course'),
    path('<int:course_id>/', views.course_detail, name='course_detail'),
    path('teacher/', views.teacher, name='teacher'),
    path('teachers/<int:pk>/', views.teacher_detail, name='teacher_detail'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('detail/', views.detail, name='detail'),
]
