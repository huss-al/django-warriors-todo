"""
URL configuration for django_to_do project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from to_do.views import registerpage, logout_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='to_do/log_in.html'), name='login'),
    path('register/', registerpage, name='register'),
    path('logout/', logout_view, name='logout'),
    path('', auth_views.LoginView.as_view(template_name='to_do/log_in.html'), name='home'),
    path('to_do/', include('to_do.urls')),
]