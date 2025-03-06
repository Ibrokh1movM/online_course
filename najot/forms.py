from django import forms
from .models import Students

class StudentStatusForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['status']
