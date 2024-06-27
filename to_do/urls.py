from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('register/', views.registerpage, name='register'),
    path('login/', views.loginpage, name='login'),
]