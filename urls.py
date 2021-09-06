from django.urls import path
from . import views
urlpatterns = [
    path('home/',views.home,name='home'),
    path('home/result/',views.result,name='result'),
    path('',views.index ,name='index'),
    path('registerteams/',views.registerteams,name='registerteams')

]