from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
#from django.contrib.auth.views import login, logout
from django.contrib.auth.views import LoginView, PasswordResetView

from . import views

app_name = 'main'
urlpatterns = [
    #path('test/', views.test, name="test"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('registration/', views.registration, name="registration"),
    path('add_user/', views.RegisterFormView.as_view(), name = "add_user"),
    path('test/', TemplateView.as_view(template_name="test.html")),
    path('login/', 
        LoginView.as_view(
            template_name='login.html'
        ), 
        name="login"
    ),
    path('password_reset/',
        PasswordResetView.as_view(
            template_name='password_change_form.html'
        ),
        name='password_reset'
    ),
    path('index/', views.index, name="index")
]