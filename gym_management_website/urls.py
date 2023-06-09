"""GYM_MANAGEMENT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from main_gym import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', views.loginuser, name='loginuser'),
    path('admin_home/', login_required(views.admin_home), name='admin_home'),
    path('logout/', views.logoutuser, name='logoutuser'),

    path('add_enquiry/', views.Add_Enquiry, name='add_enquiry'),
    path('view_enquiry/', views.View_Enquiry, name='view_enquiry'),
    path('delete_enquiry(?p<int:pid>)',
         views.Delete_Enquiry, name='delete_enquiry'),

    path('add_plan/', views.Add_Plan, name='add_plan'),
    path('view_plan/', views.View_Plan, name='view_plan'),
    path('delete_plan(?p<int:pid>)', views.Delete_Plan, name='delete_plan'),

    path('add_member/', views.Add_Member, name='add_member'),
    path('view_member/', views.View_Member, name='view_member'),
    path('delete_member(?p<int:pid>)', views.Delete_Member, name='delete_member'),

    path('mark-attendance/', views.mark_attendance, name='mark_attendance'),
    path('view-attendance/', views.view_attendance, name='view_attendance'),

    path('contact/', views.send_emails, name='send_emails'),

    path('', include('hustler.urls'))

]

