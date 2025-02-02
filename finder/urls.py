from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... مساراتك الأخرى ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 