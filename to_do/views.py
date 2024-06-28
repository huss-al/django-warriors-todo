# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from .forms import PostForm  # Import the form you'll create next
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView




# Create your views here.
@method_decorator(login_required, name='dispatch')
class PostList(generic.ListView):
    model = Post
    template_name = 'to_do/to_do.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)


# Create view for tasks
@method_decorator(login_required, name='dispatch')
class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'to_do/to_do.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user  # Assign the logged-in user as the author
        return super().form_valid(form)


# Update view for tasks
@method_decorator(login_required, name='dispatch')
class PostUpdate(generic.UpdateView):
    model = Post
    form_class = PostForm  # Replace with your form class
    template_name = 'to_do/to_do.html'
    success_url = reverse_lazy('post_list')


# Delete view for tasks
@method_decorator(login_required, name='dispatch')
class PostDelete(generic.DeleteView):
    model = Post
    template_name = 'to_do/to_do.html'
    success_url = reverse_lazy('post_list')


# Login view
def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        User = authenticate(request, username=username, password=password)
        if User is not None:
            login(request, User)
            return redirect('home') # Redirect to your main page after login
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'to_do/log_in.html')



# Registration view
def registerpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
        else:
            # Create a new user object
            new_user = User.objects.create_user(username=username)
            # Set the password for the user
            new_user.set_password(password)
            # Save the user object (this will also hash the password)
            new_user.save()
            messages.success(request, 'User successfully created, login now')
            return redirect('login') # Redirect to login page after successful registration
    return render(request, 'to_do/register.html')



def logout_view(request):
    logout(request)
    return redirect('login')