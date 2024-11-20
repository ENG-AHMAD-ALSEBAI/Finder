from django import forms
from .models import User

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'id': 'signup-password',
        'minlength': '8',
        'placeholder': 'Enter your password'
    }))
    
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'id': 'signup-password-confirm',
        'minlength': '8',
        'placeholder': 'Confirm your password'
    }))

    class Meta:
        model = User
        fields = ['full_name', 'email', 'password']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'signup-name',
                'placeholder': 'Enter your full name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'id': 'signup-email',
                'placeholder': 'Enter your email'
            })
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("كلمات المرور غير متطابقة") 

class SignInForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'id': 'signin-email',
        'placeholder': 'Enter your email'
    }))
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'id': 'signin-password',
        'placeholder': 'Enter password'
    }))