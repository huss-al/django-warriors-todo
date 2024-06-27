# views.py
from django.shortcuts import render
from django.views import generic
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.all()
    template_name = 'to_do/to_do.html'

def loginpage(request):
    return render(request, 'to_do/log_in.html', {})

def registerpage(request):
    #if request.user.is_authenticated:
        #return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        new_user = User.objects.create_user(username=username, password=password)
        new_user.save()

        messages.success(request, 'User successfully created, login now')
        return redirect('login')
    return render(request, 'to_do/register.html', {})