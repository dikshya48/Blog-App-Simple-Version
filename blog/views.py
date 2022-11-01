from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post
# posts = [
#     {
#         'author': 'John Wick',
#         'title': 'Best cars of 2020',
#         'posted_date': 'august',
#         "content": 'this is the list of all the top 20 cars made in year 2020.'
#     },
#      {
#         'author': 'Corey Bhai',
#         'title': 'Best Phones of 2020',
#         'posted_date': 'august',
#         "content": 'this is the list of all the top 20 smartphones made in year 2020.'
#     }
# ]

# Create your views here.
def home(request):
    context={
        'posts':Post.objects.all(),
        'title': 'Home'
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')