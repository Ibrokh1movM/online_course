from django.urls import path, include
from user import views

app_name = 'user'

urlpatterns = [
    path('', views.login_page, name='login_page'),
    path('register/', views.register_page, name='register_page'),
    path('forgot_password/', views.forgot_password_page, name='forgot_password'),

    path('logout/', views.logout_page, name='logout_page'),
    path('verify-email/done/', views.verify_email_done, name='verify-email-done'),
    path('verify-email-confirm/<uidb64>/<token>/', views.verify_email_confirm, name='verify-email-confirm'),
    path('verify-email/complete/', views.verify_email_complete, name='verify-email-complete'),

]
