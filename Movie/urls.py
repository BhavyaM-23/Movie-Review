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
    path('main/',views.main,name='home'),
    path('movies/',views.movies,name='movies'),
    path('shortfilms/',views.shortfilms,name='shortfilms'),
    path('genres/',views.genres,name='genres'),
    path('about/', views.about, name='about'),
path('search-movies/',views.search,name='search-movies'),
    #path for movies

    path('gully/',views.gully,name='gully'),
    path('narappa/',views.narappa,name='narappa'),
    path('msdhoni/', views.dhoni,name='msdhoni'),
    path('janathagarage/',views.janatharev,name='janatha'),
    path('alavaikuntapuramlo/',views.avrev,name='av'),
    path('jathiratnalu/',views.jathi,name='jathi'),
    path('bahubali/',views.bahubali,name='bahubali'),
    path('kabali/',views.kabali,name="kabali"),
    #paths for shortfilms

    path('sdreview/',views.sdreview,name='sd'),

    # paths for genres
    path('action/',views.action,name='action'),
    path('drama/',views.drama,name='drama'),
    path('horror/',views.horror,name='horror'),
    path('comedy/',views.comedy,name='comedy'),

]
