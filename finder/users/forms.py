from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from .models import User, UserInfo

class SignUpForm(forms.Form):
    full_name = forms.CharField(
        required=True,
        error_messages={
            'required': 'يرجى إدخال الاسم الكامل'
        },
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'أدخل اسمك الكامل'
        })
    )
    
    email = forms.EmailField(
        required=True,
        error_messages={
            'required': 'يرجى إدخال البريد الإلكتروني',
            'invalid': 'يرجى إدخال بريد إلكتروني صحيح'
        },
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'أدخل بريدك الإلكتروني'
        })
    )
    
    password = forms.CharField(
        required=True,
        min_length=8,
        error_messages={
            'required': 'يرجى إدخال كلمة المرور',
            'min_length': 'يجب أن تكون كلمة المرور 8 أحرف على الأقل'
        },
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'أدخل كلمة المرور'
        })
    )
    
    confirm_password = forms.CharField(
        required=True,
        error_messages={
            'required': 'يرجى تأكيد كلمة المرور'
        },
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'تأكيد كلمة المرور'
        })
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("هذا البريد الإلكتروني مسجل مسبقاً")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        
        if password and confirm_password and password != confirm_password:
            raise ValidationError("كلمات المرور غير متطابقة")
        return cleaned_data

    def save(self):
        data = self.cleaned_data
        full_name = data['full_name']
        names = full_name.split()
        
        if not names:
            raise ValidationError("يرجى إدخال الاسم الكامل بشكل صحيح")
        
        first_name = names[0]
        last_name = ' '.join(names[1:]) if len(names) > 1 else ''
        
        try:
            user = User.objects.create_user(
                email=data['email'],
                password=data['password'],
                full_name=full_name,
                first_name=first_name,
                last_name=last_name,
                type_subscribe='FREE'
            )
            return user
        except Exception as e:
            raise ValidationError("حدث خطأ أثناء إنشاء الحساب. الرجاء المحاولة مرة أخرى.")

class SignInForm(forms.Form):
    email = forms.EmailField(
        required=True,
        error_messages={
            'required': 'يرجى إدخال البريد الإلكتروني',
            'invalid': 'يرجى إدخال بريد إلكتروني صحيح'
        },
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'أدخل بريدك الإلكتروني'
        })
    )
    
    password = forms.CharField(
        required=True,
        error_messages={
            'required': 'يرجى إدخال كلمة المرور'
        },
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'أدخل كلمة المرور'
        })
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        
        if email and password:
            user = authenticate(username=email, password=password)
            if not user:
                raise ValidationError("البريد الإلكتروني أو كلمة المرور غير صحيحة")
            cleaned_data['user'] = user
        return cleaned_data

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
                'class': 'form-control',
                'placeholder': 'أدخل اسمك الكامل'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'أدخل بريدك الإلكتروني'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'أدخل رقم هاتفك'
            }),
            'photo': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            })
        }

class ChangePasswordForm(forms.Form):
    current_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'أدخل كلمة المرور الحالية'
    }))
    
    new_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'أدخل كلمة المرور الجديدة',
        'minlength': '8'
    }))
    
    confirm_new_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'تأكيد كلمة المرور الجديدة',
        'minlength': '8'
    }))

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get('new_password')
        confirm_new_password = cleaned_data.get('confirm_new_password')
        
        if new_password and confirm_new_password:
            if new_password != confirm_new_password:
                raise ValidationError("كلمات المرور الجديدة غير متطابقة")
        return cleaned_data