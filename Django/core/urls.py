
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("main.urls")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
