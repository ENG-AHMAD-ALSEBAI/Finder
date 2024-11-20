from django.shortcuts import redirect
from django.urls import reverse

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
        ]
        
        if not any(request.path.startswith(path) for path in public_paths):
            if not request.session.get('user_id'):
                return redirect('users:signin')
        
        response = self.get_response(request)
        return response 