"""mysite URL Configuration

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
from django.http import request
from django.urls import path
from .views import *
from profiles.views import my_recommendations_view,makedeposit
vari = 'what-if-earth-was-made-of-gold/'.lower()

urlpatterns = [
    path('', main_view,name='main-view'),
    path('airpollution/',pollution,name='air-pollution'),
    path('tuntun/', admin.site.urls),
    path('signup/', signup_view,name='signup-view'),
    path('login/',login_view,name='login'),
    path('logout/',logout_view,name='logout'),
    path('profiles/',my_recommendations_view, name='my-recs-views'),
    path('make-deposit/',makedeposit,name="make-deposit"),
    path('daily-blogs/',adds,name="daily-blogs"),
    path('withdraw/',withdraw,name="withdraw"),
    path('reset-password/',reset_passs,name='reset-password'),
    path('update/',update_passs,name='update-password'),
    path('contact/',contact,name='contact'),
    path('about/',about,name='about'),
    path('privacy/',privacy,name='privacy'),
    path('terms-and-conditons/',terms,name='terms-and-conditons'),
    path('what-if-earth-was-made-of-gold/',gold,name='gold-blogs'),
    path('tic-toc-tic-toc-timing-is-running/',water,name='tic-tac'),
   
    path('four-minutes-to-start-your-day-right/',morning,name='morning-routine'),
    path('facts-about-spirituality/',ways,name='life-ways'),
    path('drink-to-much-water-is-bad/',drink_blog,name='drink-blog'),
    path('what-if-humans-were-twice-as-intelligent/',human_blog,name='human-blog'),
    path('recommend/',recommend,name='recommend'),
    path('<str:ref_code>/',main_view,name='main-view'),
    

]
