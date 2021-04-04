from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('celebrate_birthday',views.celebrate,name='celebrate_birthday')
]
