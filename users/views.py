from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from blog.models import Post
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Acount created for {username}')
            return redirect('blog-home')
            
    else:
        form = UserCreationForm()
        
    return render(request, 'users/register.html',{'form':form})


@login_required
def profile(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request, 'users/profile.html',context)