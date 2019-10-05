from django.shortcuts import render
from .models import Blog
def blog(request):
	allblog = Blog.objects
	return render(request , 'blog.html' , {'blogs':allblog})
