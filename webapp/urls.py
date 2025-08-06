"""
URL configuration for pdf_view project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    
    path('',views.home,name='home'),
    path('admin_login',views.admin_login,name='admin_login'),
    path('emp_register',views.emp_register,name='emp_register'),
    path('emp_login', views.emp_login, name='emp_login'),
    path('logout',views.emp_logout, name='emp_logout'),
    path('dashboard',views.dashboard, name='dashboard'),
    path('email_form',views.email_form, name='email_form'),

]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
