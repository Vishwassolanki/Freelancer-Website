from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login
from hirer.models import post_job, hirer_profile
from .models import projects_bids
from user1.models import extendeduser

# Create your views here.


def admin_register(request):
	if request.method == "POST":
		adminname = request.POST['adminname']
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		email = request.POST['email']
		password = request.POST['password']
		cpassword = request.POST['cpassword']
		if password == cpassword:
			try:
				adminname == User.objects.get(username=request.POST['adminname'])
				return render(request,"admin/signup.html",{'error':"username already exist"})
			except User.DoesNotExist:	
				admin = User.objects.create_user(username=request.POST['adminname'], first_name=request.POST['first_name'],last_name=request.POST['last_name'],   email=request.POST['email'], password=request.POST['password'])
				auth.login(request,admin)
				f3=extendeduser(is_admin1="1",is_hirer="0", is_user="0", User =request.user)
				f3.save()
				return redirect('/admin1/dashboard')
		else:
			return render(request, "admin/signup.html",{'error':"password and confirm password must be same. "})		

def admin_login(request):
	if request.method == "POST":
		username = request.POST['adminname']
		pwd = request.POST['password']
		user = auth.authenticate(request, username=username, password=pwd)
		if user is not None:
			auth.login(request, user)
			return redirect('/admin1/dashboard')
		else:
			return render(request, "admin/login1.html",{'error':"username or password is invalid."})
	else: return render(request,"admin/login1.html")	

def admin_logout(request):
	auth.logout(request)
	return redirect('/admin1/login1')


def dashboard(request):
	if request.user.is_authenticated:
		return render(request, 'admin/dashboard.html')
	else:
		return render(request, 'admin/login1.html')	

def projects_list(request):
	if request.user.is_authenticated:
		return render(request, 'admin/projects_list.html')
	else:
		return render(request, 'admin/login1.html')	

def freelancer(request):
	if request.user.is_authenticated:
		return render(request, 'admin/freelancer.html')
	else:
		return render(request, 'admin/login1.html')	

def hirer(request):
	if request.user.is_authenticated:
		hirer = hirer_profile.objects.filter(userid=request.user)
		return render(request, 'admin/hirer.html', {'data': hirer})
	else:
		return render(request, 'admin/login1.html')	
	

def payment_section(request):
	if request.user.is_authenticated:
		return render(request, 'admin/payment_section.html')
	else:
		return render(request, 'admin/login1.html')

def projectsbids(request):
	if request.user.is_authenticated:
		bids_data = projects_bids.objects.all()
		project_info = post_job.objects.all()
		return render(request, 'admin/projects_bids.html',{'bids_data' : bids_data})
	else:
		return render(request, 'admin/login1.html')

def reports(request):
	if request.user.is_authenticated:
		return render(request, 'admin/reports.html')
	else:
		return render(request, 'admin/login1.html')

def login(request):
	return render(request, 'admin/login1.html')

def signup(request):
	return render(request, 'admin/signup.html')	

