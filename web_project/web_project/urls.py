"""web_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include, re_path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from polls import views as polls_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('boards/', include('boards.urls')),
    path('accounts/', include('accounts.urls')),
    path('catalog/', include('catalog.urls')),
    #path('', RedirectView.as_view(url='catalog/', permanent=True)),

    path('', polls_views.index, name='home'),
    
    path('winter_winnpy/', polls_views.winter_winnpy, name='winter_winnpy'),
    path('winter_univer/', polls_views.winter_univer, name='winter_univer'),
    path('face_recognition/', polls_views.face_recognition, name='face_recognition'),


]

urlpatterns += staticfiles_urlpatterns()