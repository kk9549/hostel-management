"""hms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from selections import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='register'),
    path('reg_form/', views.register, name='reg_form'),
    path('login/', views.user_login, name='login'),
    path('warden_login/', views.warden_login, name='warden_login'),
    path('warden_dues/', views.warden_dues, name='warden_dues'),
    path('warden_add_due/', views.warden_add_due, name='warden_add_due'),
    path('warden_remove_due/', views.warden_remove_due, name='warden_remove_due'),
    path('hostels/<slug:hostel_name>/', views.hostel_detail_view, name='hostel'),
    path('login/edit/', views.edit, name='edit'),
    path('login/select/', views.select, name='select'),
    path('logout/', views.logout_view, name='logout'),
    path('reg_form/login/edit/', views.edit, name='update'),
    path('BH5_GroundFloor/', views.BH5_GroundFloor, name='BH5_GroundFloor'),
    path('BH5_Floor1/', views.BH5_Floor1, name='BH5_Floor1'),
    path('BH5_Floor2/', views.BH5_Floor2, name='BH5_Floor2'),
    path('BH5_Floor3/', views.BH5_Floor3, name='BH5_Floor3'),
    path('BH5_Floor4/', views.BH5_Floor4, name='BH5_Floor4'),
    path('BH5_Floor5/', views.BH5_Floor5, name='BH5_Floor5'),
    path('BH5_Floor6/', views.BH5_Floor6, name='BH5_Floor6'),
]

