from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.user_index),
    path('about', views.about),
    path('contact', views.contact),
    path('work', views.work),
    path('web_design', views.web_design),
    path('web_dev', views.web_dev),
    path('graphic_design', views.graphic_design),
    path('writing', views.writing),
    path('user_login', views.user_login),
    path('logout', views.user_logout),
    path('user_register', views.user_register),
    path('apply_bid', views.apply_bid),
]
