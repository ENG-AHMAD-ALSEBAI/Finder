import os
import django
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'finder.settings')
django.setup()

from users.models import User

def create_superuser():
    try:
        superuser = User.objects.create_superuser(
            email='admin@example.com',
            password='admin123456',
            full_name='Admin User'
        )
        print('Superuser created successfully!')
    except Exception as e:
        print(f'Error creating superuser: {e}')

if __name__ == '__main__':
    create_superuser()
