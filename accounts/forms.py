from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    username= forms.CharField(max_length=250, widget=forms.TextInput(attrs={ 'class' :'form-control'}))
    first_name= forms.CharField(max_length=250, widget=forms.TextInput(attrs={ 'class' :'form-control'}))
    last_name= forms.CharField(max_length=250, widget=forms.TextInput(attrs={ 'class' :'form-control'}))
    password1= forms.CharField(max_length=250, label='password',widget=forms.PasswordInput(attrs={ 'class' :'form-control'}))
    email= forms.CharField(max_length=250, widget=forms.TextInput(attrs={ 'class' :'form-control'}))
    password2= forms.CharField(max_length=250, label='password',widget=forms.PasswordInput(attrs={ 'class' :'form-control'}))
    shopOwner = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={ 'class' :'form-check-input'}))
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'shopOwner'
        )

    # save will return an instance of user model at the end
    def save(self,commit=True):
         user=super(SignUpForm,self).save(commit=False)
         user.email=self.cleaned_data['email']
         user.first_name=self.cleaned_data['first_name']
         user.last_name=self.cleaned_data['last_name']
         if commit:
             user.save()
         return user

class LoginForm(forms.Form):
    username = forms.CharField(max_length=250, widget=forms.TextInput(attrs={ 'class' :'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={ 'class' :'form-control'}))