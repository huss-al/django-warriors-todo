# views.py
from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.all()
    template_name = 'to_do/to_do.html'

def loginpage(request):
    return render(request, 'to_do/log_in.html', {})

def registerpage(request):
    return render(request, 'to_do/register.html', {})