from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('friends_app.urls')),
    path('', TemplateView.as_view(template_name='home.html')),
]
