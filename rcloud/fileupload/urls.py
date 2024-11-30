from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import file_upload_view, upload_success_view

urlpatterns = [
    path('upload/', file_upload_view, name='file_upload'),
    path('success/', upload_success_view, name='success'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)