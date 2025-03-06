from django import forms
from .models import Registration, Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'image', 'category', 'lessons_count']


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['name', 'email', 'course']

    course = forms.ModelChoiceField(
        queryset=Course.objects.all(),
        empty_label="Select a course",
        widget=forms.Select(attrs={'class': 'custom-select border-0 px-4', 'style': 'height: 47px;'})
    )
