from .views import *
from django.urls import path
app_name = 'App_Account'

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('logout/', user_logout, name='logout'),


]

