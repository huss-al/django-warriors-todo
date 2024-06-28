from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('register/', views.registerpage, name='register'),
    path('login/', views.loginpage, name='login'),
    path('create/', views.PostCreate.as_view(), name='post_create'),
    path('post/<int:pk>/delete/', views.PostDelete.as_view(), name='post_delete'),
    path('post/<int:pk>/started/', views.PostStarted.as_view(), name='post_started'),
    path('post/<int:pk>/complete/', views.PostComplete.as_view(), name='post_complete'),
    path('post/<int:pk>/to_do/', views.Post_to_do.as_view(), name='post_to_do'),


    path('log_out_confirmation/', views.log_out_confirmation, name='log_out_confirmation'),

]