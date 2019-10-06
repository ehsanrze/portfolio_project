from django.shortcuts import render , get_object_or_404
from .models import Blog
def blog(request):
		allblog = Blog.objects
		return render(request , 'blog.html' , {'blogs':allblog})
	

def detail_blog(request , id):
		detail = get_object_or_404(Blog , pk = id )
		return render(request , 'detail.html' , {'blog':detail})