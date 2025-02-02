from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from .forms import SignUpForm, SignInForm, AccountInfoForm, UserUpdateForm, ChangePasswordForm
from .models import User, UserInfo
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.
@csrf_protect
def signin(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            login(request, user)
            
            # Store user info in session
            request.session['user_id'] = user.id_user
            request.session['user_email'] = user.email
            request.session.set_expiry(86400)  # 24 hours
            
            messages.success(request, 'تم تسجيل الدخول بنجاح!')
            return redirect('pages:home')
    else:
        form = SignInForm()
    
    return render(request, 'signin-light.html', {'form': form})

@csrf_protect
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        try:
            if form.is_valid():
                user = form.save()
                login(request, user)
                
                # Store user info in session
                request.session['user_id'] = user.id_user
                request.session['user_email'] = user.email
                request.session.set_expiry(86400)  # 24 hours
                
                messages.success(request, 'تم إنشاء حسابك بنجاح!')
                return redirect('pages:home')
        except Exception as e:
            messages.error(request, str(e))
    else:
        form = SignUpForm()
    
    return render(request, 'signup-light.html', {'form': form})

def signout(request):
    # Clear all session data and log out
    logout(request)
    request.session.flush()
    messages.success(request, 'تم تسجيل الخروج بنجاح')
    return redirect('pages:home')

def login_required_custom(view_func):
    def wrapper(request, *args, **kwargs):
        if 'user_id' not in request.session or not request.user.is_authenticated:
            messages.error(request, 'يجب تسجيل الدخول أولاً')
            return redirect('users:signin')
        return view_func(request, *args, **kwargs)
    return wrapper

@login_required_custom
def account_info(request):
    try:
        user = User.objects.get(id_user=request.session['user_id'])
        user_info, created = UserInfo.objects.get_or_create(user=user)

        if request.method == 'POST':
            user_form = UserUpdateForm(request.POST, request.FILES, instance=user)
            info_form = AccountInfoForm(request.POST, instance=user_info)
            
            if user_form.is_valid() and info_form.is_valid():
                if 'photo' in request.FILES:
                    user.photo = request.FILES['photo']
                
                user_form.save()
                info_form.save()
                messages.success(request, 'تم تحديث المعلومات بنجاح')
                return redirect('users:account_info')
        else:
            user_form = UserUpdateForm(instance=user)
            info_form = AccountInfoForm(instance=user_info)
        
        context = {
            'user': user,
            'user_info': user_info,
            'user_form': user_form,
            'info_form': info_form
        }
        return render(request, 'real-estate-account-info.html', context)
    except User.DoesNotExist:
        messages.error(request, 'حدث خطأ في العثور على بيانات المستخدم')
        return redirect('users:signin')

@login_required_custom
def account_security(request):
    try:
        user = User.objects.get(id_user=request.session['user_id'])
        
        if request.method == 'POST':
            form = ChangePasswordForm(request.POST)
            if form.is_valid():
                current_password = form.cleaned_data['current_password']
                new_password = form.cleaned_data['new_password']
                
                if check_password(current_password, user.password):
                    user.password = make_password(new_password)
                    user.save()
                    messages.success(request, 'تم تغيير كلمة المرور بنجاح')
                    return redirect('users:account_security')
                else:
                    messages.error(request, 'كلمة المرور الحالية غير صحيحة')
        else:
            form = ChangePasswordForm()
        
        return render(request, 'real-estate-account-security.html', {
            'form': form,
            'user': user
        })
    except User.DoesNotExist:
        messages.error(request, 'حدث خطأ في العثور على بيانات المستخدم')
        return redirect('users:signin')

@login_required_custom
def account_notifications(request):
    try:
        user = User.objects.get(id_user=request.session['user_id'])
        return render(request, 'real-estate-account-notifications.html', {'user': user})
    except User.DoesNotExist:
        messages.error(request, 'حدث خطأ في العثور على بيانات المستخدم')
        return redirect('users:signin')
