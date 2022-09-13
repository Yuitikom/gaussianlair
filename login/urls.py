from django.urls import path
from .  import views

urlpatterns = [
    path('', views.loginuser, name='login'),
    path('logout', views.logoutuser, name='logout')
]