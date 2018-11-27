from django.shortcuts import render
# from django.http import HttpResponse
from .models import Post
from django.contrib.auth.decorators import login_required

# posts = [
# 			{
# 				'title': 'Some title1',
# 				'author': 'Author 1',
# 				'date': 'Today',
# 				'content': 'Content1'
# 			},
# 			{
# 				'title': 'Some title2',
# 				'author': 'Author 2',
# 				'date': 'Tomorrow',
# 				'content': 'Content2'
# 			},
# 			{
# 				'title': 'Some title3',
# 				'author': 'Author 3',
# 				'date': 'Tomorrow',
# 				'content': 'Content3'
# 			}
# 		]

# Create your views here.
@login_required
def home(request):
	context = {
		'posts': Post.objects.all(),
		'title': 'Home'
	}
	return render(request, 'blog/home.html', context)


@login_required
def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})


@login_required
def contact(request):
	return HttpResponse('<a href="https://www.github.com/okaysidd">Contact Us</a>')
