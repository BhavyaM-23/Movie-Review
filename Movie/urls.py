"""Movie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.main),
    path('main/',views.main),
    path('movies/',views.movies),
    path('shortfilms/',views.shortfilms),
    path('genres/',views.genres),
    path('about/',views.about),
    #paths from movies
    path('movies/main/',views.main),
    path('movies/shortfilms/',views.shortfilms),
    path('movies/genres/',views.genres),
    path('movies/about/',views.about),
    #paths from shortfilms
    path('shortfilms/main/',views.main),
    path('shortfilms/movies/',views.movies),
    path('shortfilms/genres/',views.genres),
    path('shortfilms/about/',views.about),
    path('shortfilms/sdreview/',views.sdreview),
    #paths from genres
    path('genres/main/',views.main),
    path('genres/movies/',views.movies),
    path('genres/shortfilms/',views.shortfilms),
    path('genres/about/',views.about),
    #paths from about
    path('about/main/',views.main),
    path('about/movies/',views.movies),
    path('about/shortfilms/',views.shortfilms),
    path('about/genres/',views.genres),
]
