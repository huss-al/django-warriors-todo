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
from .forms import PostForm, DeleteForm # Import the form you'll create next
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView




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
class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    form_class = DeleteForm
    template_name = 'to_do/to_do.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user  # Assign the logged-in user as the author
        return super().form_valid(form)

#started view
class PostStarted(LoginRequiredMixin, CreateView):
    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        post.status = 2  # Update status to 'started'
        post.save()
        return redirect('home')  # Redirect to post list or another appropriate view

#complete view
class PostComplete(LoginRequiredMixin, CreateView):
    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        post.status = 3  # Update status to 'complete'
        post.save()
        return redirect('home')  # Redirect to post list or another appropriate view

#to-do view
class Post_to_do(LoginRequiredMixin, CreateView):
    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        post.status = 1  # Update status to 'to-do'
        post.save()
        return redirect('home')  # Redirect to post list or another appropriate view
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


#delete
def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('/to_do')  # Redirect to a URL name representing post list or any other appropriate view
    # Handle GET request if needed, for confirmation or other actions
    # Typically, you would render a confirmation template for deletion
    return render(request, 'delete_confirmation.html', {'post': post})

def log_out_confirmation(request):
    return render(request, 'to_do/log_out_confirmation.html')

