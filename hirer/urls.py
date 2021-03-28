from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('post_a_job', views.post_a_job),
    path('post_job', views.postjob),
    path('freelance_list', views.freelance_list),
    path('payment_status', views.payment_status),
    path('profile', views.profile),
    path('profile1', views.profile1),
    path('work_status', views.work_status),
    path('', views.hirer_login),
    path('signup', views.signup),
    path('hirer_register', views.hirer_register),
    path('hirer_login', views.hirer_login),
    path('logout', views.hirer_logout),
] 
