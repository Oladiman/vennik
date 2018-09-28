from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_Name',
            'last_Name',
            'Password1',
            'Password2',
        )
    def save(self,commit=True):
        user = super(registrationForm,self).save(commit=False)
        user.first_Name = self.cleaned_data['first_Name']
        user.last_Name = self.cleaned_data['last_Name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return User