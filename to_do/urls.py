from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('register/', views.registerpage, name='register'),
    path('login/', views.loginpage, name='login'),
    path('create/', views.PostCreate.as_view(), name='post_create'),
    path('log_out_confirmation/', views.log_out_confirmation, name='log_out_confirmation'),
]