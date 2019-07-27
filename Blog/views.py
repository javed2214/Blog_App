from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import BlogApp, Comment
from django.contrib.auth.models import User
from django.contrib import auth
from django.utils import timezone
from django.contrib.auth.decorators import login_required

rs = 0
ps = 0

def index(request):
	return render(request, 'Blog/index.html')


def showblog(request):
	blog = BlogApp.objects.all()
	context = {'blog':blog}
	return render(request, 'Blog/showblog.html', context)


def detail(request, blog_id):
	global rs
	rs = blog_id
	info = BlogApp.objects.all()
	data = BlogApp.objects.get(pk = blog_id)
	ds = data.user
	cmnt = info[blog_id - 1].comment_set.all()
	us = request.user.username
	px = ""
	cx = 0
	if(len(us) == 0):
		px = ""
		return redirect('signup')
	else:
		px = "Autor: "+us
		cx = 1
		context = {'blog':data, 'cmnt':cmnt, 'user':px, 'cx':cx, 'us':us, 'ds':ds}
		return render(request, 'Blog/detail.html', context)


def comment(request):
	name = request.user.username
	comment = request.POST['comment']
	d = Comment(name = name, comment = comment, blog_id = rs)
	d.save()
	return detail(request, rs)


def delete(request, cmnt_id):
	data = Comment.objects.get(pk = cmnt_id)
	data.delete()
	return detail(request, rs)


def signup(request):
	if(request.method == 'POST'):
		if(request.POST['password1'] == request.POST['password2']):
			try:
				user = User.objects.get(username = request.POST['username'])
				return render(request, 'Blog/signup.html', {'error': 'Username is Already Taken!'})
			except User.DoesNotExist:
				user = User.objects.create_user(request.POST['username'], password = request.POST['password1'])
				auth.login(request, user)
				return render(request, 'Blog/signup.html', {'errorr': 'User Created Successfully!'})
		else:
			return render(request, 'Blog/signup.html', {'error': 'Password doesn\'t Matched!'})
	else:
		return render(request, 'Blog/signup.html')



def login(request):
	if(request.method == 'POST'):
		user = auth.authenticate(username = request.POST['username'], password = request.POST['password'])
		if(user is not None):
			auth.login(request, user)
			user = request.POST['username']
			return logged_in(request)
		else:
			return render(request, 'Blog/login.html', {'error': 'Username or Password is Invalid!'})
	else:
		return render(request, 'Blog/login.html')


def logout(request):
	if(request.method == 'POST'):
		auth.logout(request)
		return redirect('index')


@login_required
def logged_in(request):
	blog = BlogApp.objects.all()
	us = User.objects.all()
	user_id = User.id
	data = us[request.user.id - 1].blogapp_set.all()
	x = -1
	if(data.count() != 0):
		x = 1
	else:
		x = 0
	print(x)
	context = {'blog':data, 'x':x}
	return render(request, 'Blog/logged_in.html', context)

@login_required
def create(request):
	return render(request, 'Blog/create.html')

@login_required
def postarticle(request):
	data = BlogApp()
	data.title = request.POST['title']
	data.image = request.FILES['image']
	data.body = request.POST['body']
	data.pub_date = timezone.datetime.now()
	data.user = request.user

	data.save()

	return render(request, 'Blog/posted.html')


def deletearticle(request, article_id):
	fam = BlogApp.objects.get(pk = article_id)
	fam.delete()
	return logged_in(request)


def updatearticle(request, article_id):
	data = BlogApp.objects.get(pk = article_id)
	global ps
	ps = data.image
	context = {'blog':data}
	return render(request, 'Blog/updatearticle.html', context)


def updated(request, article_id):
	data = BlogApp.objects.get(pk = article_id)
	data.title = request.POST['title']
	
	filepath = request.FILES.get('image', False)
	if filepath == False:
		data.image = ps
	else:
		data.image = request.FILES['image']

	data.body = request.POST['body']

	data.save()

	return render(request, 'Blog/updated.html')


def upvote(request, blog_id):
	data = BlogApp.objects.get(pk = blog_id)
	us = str(request.user.username)
	ls = us.split(' ')
	if(len(ls) > 1):
		us = ""
		for b in ls:
			us += b
	up = data.user_upvoted
	ss = ""
	li = up.split(' ')
	print(ss)
	flag = 0
	for s in li:
		if(s == us):
			li.remove(us)
			data.upvote -= 1
			flag = 1
			break;
	if(flag == 0):
		li.append(us)
		data.upvote += 1
	for d in li:
		ss+=d+" "
	data.user_upvoted = ss

	data.save()

	return detail(request, blog_id)