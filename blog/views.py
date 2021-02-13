from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.

def all_blogs(request):
    dailyfeed = DailyFeed.objects.all()
    newpost = NewPost.objects.all()
    context = {'dailyfeed':dailyfeed, 'newpost':newpost }
    return render(request, 'blog/all_blog.html', context)


