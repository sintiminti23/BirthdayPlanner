from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path(path("auth/", include("Birthday_Planner_Python_Web_Framework.authentication.urls")),)

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
