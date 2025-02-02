from django.shortcuts import redirect
from django.urls import reverse
from .models import User
from django.contrib.auth import login

class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        public_paths = [
            '/users/signin/',
            '/users/signup/',
            '/admin/',
            '/',
            '/home/',
            '/properties/home/',
            '/properties/catalog_sale/',
            '/properties/catalog_rent/',
            '/properties/single_v1/',
            '/properties/single_v2/',
            '/static/',
            '/media/',
        ]
        
        # Check if the path is public
        if not any(request.path.startswith(path) for path in public_paths):
            user_id = request.session.get('user_id')
            
            # If user is not authenticated
            if not user_id:
                return redirect('users:signin')
            
            # If user is in session but not in request.user, log them in
            if not request.user.is_authenticated:
                try:
                    user = User.objects.get(id_user=user_id)
                    login(request, user)
                except User.DoesNotExist:
                    request.session.flush()
                    return redirect('users:signin')
        
        response = self.get_response(request)
        return response