from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from .models import extendeduser, user_profile
from django.contrib.auth import authenticate, login
from hirer.models import post_job, hirer_profile
from django.core.files.storage import FileSystemStorage
from admin1.models import projects_bids


# Create your views here.

def user_index(request):
    return render(request, 'user/login.html')


def user_register(request):
    if request.method == "POST":
        username = request.POST['username']
        myfile1 = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(myfile1.name, myfile1)
        url1 = fs.url(filename)
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        Qualification = request.POST['Qualification']
        tech_exp = request.POST['tech_exp']
        exp = request.POST['exp']
        charges = request.POST['charges']
        userid = request.user
        if password == cpassword:
            try:
                username == User.objects.get(username=request.POST['username'])
                return render(request, 'user/signup.html', {'error': 'User name is already exist..'})
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['username'], email=request.POST['email'],
                                                password=request.POST['password'], first_name=request.POST['fname'],
                                                last_name=request.POST['lname'])
                auth.login(request, user)
                # to store userProfile
                store = user_profile(image=url1, fname=first_name, lname=last_name, email=email,
                                     Qualification=Qualification,
                                     tech_exp=tech_exp, exp=exp, rate_hr=charges, userid=userid)
                store.save()
                # var = extendeduser(is_admin1="0", is_hirer="0", is_user="1", User=request.user)
                # var.save()
                return redirect('/user1')
        else:
            return render(request, '/user/signup.html', {'error': 'Password does not match.'})
    else:
        return render(request, 'user/signup.html')


def user_login(request):
    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/user1/about')
        else:
            return render(request, "user/login.html", {'error': "username or password is invalid."})

    else:
        return render(request, 'user/login.html')


def user_logout(request):
    auth.logout(request)
    return redirect('/user1/user_login')


def about(request):
    user = user_profile.objects.filter(userid=request.user)
    return render(request, 'user/about.html', {'data': user})


def work(request):
    wlist = post_job.objects.all()
    return render(request, 'user/work.html', {'data': wlist})


def contact(request):
    return render(request, 'user/contact.html')


def web_design(request):
    return render(request, 'user/web_design.html')


def web_dev(request):
    return render(request, 'user/web_dev.html')


def graphic_design(request):
    return render(request, 'user/graphic_design.html')


def writing(request):
    return render(request, 'user/writing.html')


def apply_bid(request):
    if request.method == "POST":
        jobid = request.POST['jobid']
        comments = request.POST['input_comments']
        store = projects_bids(job_id=jobid, comments=comments, userid=request.user)
        store.save()
        return redirect('/user1/work')
    else:
        return render(request, 'user/work.html')
