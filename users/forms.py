from django import forms
from .models import User, UserInfo

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

class AccountInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['short_bio', 'company_name', 'address', 'facebook', 'linkedin', 'twitter', 'instagram']
        widgets = {
            'short_bio': forms.Textarea(attrs={
                'class': 'form-control',
                'id': 'account-bio',
                'rows': '6',
                'placeholder': 'اكتب نبذة عنك هنا. سيتم عرضها في ملفك الشخصي العام.'
            }),
            'company_name': forms.TextInput(attrs={
                'class': 'form-control mt-3',
                'placeholder': 'أدخل اسم الشركة'
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control mt-3',
                'placeholder': 'أدخل العنوان'
            }),
            'facebook': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'حساب الفيسبوك الخاص بك'
            }),
            'linkedin': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'حساب لينكد إن الخاص بك'
            }),
            'twitter': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'حساب تويتر الخاص بك'
            }),
            'instagram': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'حساب انستجرام الخاص بك'
            })
        }

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['full_name', 'email', 'phone_number', 'photo']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control mt-3',
                'data-bs-binded-element': '#name-value',
                'data-bs-unset-value': 'غير محدد'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control mt-3',
                'data-bs-binded-element': '#email-value',
                'data-bs-unset-value': 'غير محدد'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control mt-3',
                'data-bs-binded-element': '#phone-value',
                'data-bs-unset-value': 'غير محدد'
            }),
            'photo': forms.FileInput(attrs={
                'class': 'file-uploader bg-secondary',
                'accept': 'image/png, image/jpeg',
                'data-label-idle': '<i class="d-inline-block fi-camera-plus fs-2 text-muted mb-2"></i><br><span class="fw-bold">تغيير الصورة</span>',
                'data-style-panel-layout': 'compact',
                'data-image-preview-height': '160',
                'data-image-crop-aspect-ratio': '1:1',
                'data-image-resize-target-width': '200',
                'data-image-resize-target-height': '200'
            })
        }