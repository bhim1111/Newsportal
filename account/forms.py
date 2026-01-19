from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
class LoginForm(AuthenticationForm):
    username=forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "username"}
        )
    )
    password=forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "password"}
        )
    )
    
class RegistrationForm(UserCreationForm):
    email=forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Enter your email"}
            
        ),
    )
    
    username=forms.CharField(
        required=True,
        max_length=200,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter your username"}
        ),
    )
    
    password1=forms.CharField(
        label="password",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Enter your password1"}
        ),
    )
    
    password2=forms.CharField(
        label="password",
        widget=forms.PasswordInput(
            attrs={"class":"form-control", "placeholder":"Confirm password"}
            
        ),
    )
    
    class Meta(UserCreationForm.Meta):
        model=User
        fields= ("username", "email" )
        
        
        def clean_email(self):
            email = self.cleaned_data.get("email")
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("An account with this email already exists.")
            return email
        
        
        
        
        
        