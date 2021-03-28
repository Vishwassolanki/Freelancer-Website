from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.dashboard),
    path('projects_list', views.projects_list),
    path('freelancer', views.freelancer),
    path('hirer', views.hirer),
    path('payment_section', views.payment_section),
    path('projects_bids', views.projectsbids),
    path('reports', views.reports),
    path('signup', views.signup),
    path('admin_register', views.admin_register),
    path('', views.admin_login),
    path('logout', views.admin_logout),
    path('login1', views.login),
    path('admin_login', views.admin_login),



]
