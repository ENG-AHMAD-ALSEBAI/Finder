from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignUpForm, SignInForm
from django.contrib.auth.hashers import make_password, check_password
from .models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def signin(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            try:
                user = User.objects.get(email=email)
                if check_password(password, user.password):
                    request.session['user_id'] = user.id_user
                    request.session['user_name'] = user.full_name
                    messages.success(request, 'تم تسجيل الدخول بنجاح!')
                    return redirect('pages:home')
                else:
                    messages.error(request, 'كلمة المرور غير صحيحة')
            except User.DoesNotExist:
                messages.error(request, 'البريد الإلكتروني غير مسجل')
    else:
        form = SignInForm()
    
    return render(request, 'signin-light.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # حفظ البيانات مع تشفير كلمة المرور
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])
            user.type_subscribe = 'FREE'  # تعيين نوع الاشتراك الافتراضي
            # تقسيم الاسم الكامل إلى الاسم الأول والأخير
            full_name = form.cleaned_data['full_name'].split()
            if len(full_name) > 1:
                user.first_name = full_name[0]
                user.last_name = ' '.join(full_name[1:])
            else:
                user.first_name = full_name[0]
                user.last_name = ''
            
            user.save()
            messages.success(request, 'تم إنشاء حسابك بنجاح!')
            return redirect('users:signin')
        else:
            messages.error(request, 'الرجاء تصحيح الأخطاء أدناه.')
    else:
        form = SignUpForm()
    
    return render(request, 'signup-light.html', {'form': form})

@login_required(login_url='signin')
def account_security(request):
    return render(request, 'real-estate-account-security.html')

@login_required(login_url='signin')
def account_info(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = User.objects.get(id_user=user_id)
        return render(request, 'real-estate-account-info.html', {'user': user})
    return redirect('signin')

@login_required(login_url='signin')
def account_notifications(request):
    return render(request, 'real-estate-account-notifications.html')

def signout(request):
    request.session.flush()
    messages.success(request, 'تم تسجيل الخروج بنجاح')
    return redirect('signin')

