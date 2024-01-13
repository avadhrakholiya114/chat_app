from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('<str:room>/', room, name='room'),
    path('checkview', checkview, name="checkview"),

]
