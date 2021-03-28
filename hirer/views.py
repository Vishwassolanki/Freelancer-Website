from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login
from user1.models import extendeduser, user_profile
from .models import post_job, hirer_profile
from django.core.files.storage import FileSystemStorage


# Create your views here.


def hirer_register(request):
    if request.method == "POST":
        hirername = request.POST['hirername']
        myfile1 = request.FILES['pimage']
        fs = FileSystemStorage()
        filename = fs.save(myfile1.name, myfile1)
        url1 = fs.url(filename)
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        company_name = request.POST['company_name']
        email = request.POST['email']
        contact = request.POST['contact']
        userid = request.user

        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            try:
                hirername == User.objects.get(username=request.POST['hirername'])
                return render(request, "hirer/signup.html", {'error': 'username already exist'})
            except User.DoesNotExist:
                hirer = User.objects.create_user(username=request.POST['hirername'],
                                                 first_name=request.POST['first_name'],
                                                 last_name=request.POST['last_name'], email=request.POST['email'],
                                                 password=request.POST['password'])
                auth.login(request, hirer)
                f2 = extendeduser(is_admin1="0", is_hirer="1", is_user="0", User=request.user)
                f2.save()
                store = hirer_profile(pimage=url1, fname=first_name, lname=last_name, company_name=company_name,
                                      email=email, contact=contact, userid=userid)
                store.save()
                return redirect('/hirer/profile')
        else:
            return render(request, "hirer/signup.html", {'error': "password and confirm password must be same"})


def hirer_login(request):
    if request.method == "POST":
        hirername = request.POST['hirername']
        pwd = request.POST['password']
        user = auth.authenticate(request, username=hirername, password=pwd)
        if user is not None:
            auth.login(request, user)
            return redirect('/hirer/profile')
        else:
            return render(request, "hirer/login.html", {'error': "username or password is invalid."})
    else:
        return render(request, "hirer/login.html")


def hirer_logout(request):
    auth.logout(request)
    return redirect('/hirer/hirer_login')


def postjob(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            projectname = request.POST['project_name']
            projectdescription = request.POST['project_description']
            category = request.POST['category']
            budget = request.POST['budget']
            starttime = request.POST['start_time']
            endtime = request.POST['end_time']
            ftech = request.POST['ftech']
            btech = request.POST['btech']
            userid = request.user
            store = post_job(project_name=projectname, project_description=projectdescription, category=category,
                             budget=budget, start_time=starttime, end_time=endtime, ftech=ftech, btech=btech,
                             userid=userid)
            store.save()
        return render(request, 'hirer/work_status.html')
    else:
        return render(request, 'hirer/login.html')


def post_a_job(request):
    if request.user.is_authenticated:
        return render(request, 'hirer/post_a_job.html')
    else:
        return render(request, 'hirer/login.html')


def freelance_list(request):
    if request.user.is_authenticated:
        flist = user_profile.objects.filter(userid=request.user)
        return render(request, 'hirer/freelance_list.html', {'data': flist})
    else:
        return render(request, 'hirer/login.html')


def payment_status(request):
    if request.user.is_authenticated:
        return render(request, 'hirer/payment_status.html')
    else:
        return render(request, 'hirer/login.html')


def profile(request):
    if request.user.is_authenticated:
        hirer = hirer_profile.objects.filter(userid=request.user)
        return render(request, 'hirer/profile.html', {'data': hirer})
    else:
        return render(request, 'hirer/login.html')


def profile1(request):
    return render(request, 'hirer/profile1.html')


def work_status(request):
    if request.user.is_authenticated:
        hirer = post_job.objects.filter(userid=request.user)
        return render(request, 'hirer/work_status.html', {'data': hirer})
    else:
        return render(request, 'hirer/login.html')


def logout(request):
    return render(request, 'hirer/login.html')


def signup(request):
    return render(request, 'hirer/signup.html')
