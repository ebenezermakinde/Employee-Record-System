"""
Definition of forms.
"""

from django import forms
from django.core.validators import validate_email

from .models import employeebiodata

#Choices for Gender
EMPLOYEE_GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

class employeeForm(forms.Form):
    firstname = forms.CharField(label='First Name*', max_length=220, widget=forms.TextInput(attrs={'class':'form-control'}))
    lastname = forms.CharField(label='Last Name*', max_length=220, widget=forms.TextInput(attrs={'class':'form-control'}))
    gender = forms.CharField(label='Gender*', max_length=1, widget=forms.RadioSelect(choices=EMPLOYEE_GENDER))
    email = forms.EmailField(label='Email*', max_length=60, widget=forms.TextInput(attrs={'class':'form-control'}))
   

    def clean_email(self):
        email = self.cleaned_data['email']
        if employeebiodata.objects.filter(email=email).exists():
            raise forms.ValidationError('This email has been taken')
        return email

