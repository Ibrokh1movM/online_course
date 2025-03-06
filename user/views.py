from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from user.forms import LoginForm
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from user.custom_token import account_activation_token
from django.core.mail import EmailMessage


User = get_user_model()


def login_page(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                return redirect('online_courses:index')
            else:
                messages.add_message(request,
                                     messages.ERROR,
                                     'Invalid login')
    context = {
        'form': form
    }
    return render(request, 'user/login.html', context=context)


from django.shortcuts import render
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from user.custom_token import account_activation_token
from .forms import RegisterForm


def register_page(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            email = user.email
            subject = "Verify Email"
            message = render_to_string('user/email-verification/verify_email_message.html', {
                'request': request,
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })

            email_message = EmailMessage(subject, message, to=[email])
            email_message.content_subtype = 'html'
            email_message.send()

            return render(request, 'user/email-verification/verify_email_done.html', {'email': user.email})

        else:
            print("Formda xatoliklar mavjud:", form.errors)
            return render(request, 'user/register.html', {'form': form})

    form = RegisterForm()
    return render(request, 'user/register.html', {'form': form})


def verify_email_confirm(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save()
        messages.success(request, 'Your email has been verified.')

        user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(request, user)
        return redirect('user:verify-email-complete')
    else:
        messages.warning(request, 'The link is invalid.')
    return render(request, 'user/email-verification/verify_email_confirm.html')


def verify_email_complete(request):
    return render(request, 'user/email-verification/verify_email_complete.html')

def verify_email_done(request):
    return render(request, 'user/email-verification/verify_email_done.html')

def forgot_password_page(request):
    return render(request, 'user/forgot_password.html')

def logout_page(request):
    logout(request)
    return redirect('online_courses:index')
