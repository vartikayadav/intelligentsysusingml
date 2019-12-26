from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):
    email=forms.EmailField(required=True)#to customize as we want email to be there
    class Meta:
        model=User
        fields=[
        'username',
        'first_name',
        'last_name',
        'email',
        'password1',
        'password2'
        ]
    def save(self,commit=True):
        #commit true means data is now ready to be saved and stored
        user=super(UserCreateForm,self).save(commit=False)
        user.first_name=self.cleaned_data['first_name']
        user.last_name=self.cleaned_data['last_name']
        user.email=self.cleaned_data['email']
        if  commit:
            user.save()
        return user
