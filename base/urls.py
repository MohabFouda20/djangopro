from django.urls import path
from . import views

urlpatterns = [
    path('',views.home , name= "name" ),
    path ('king/<str:pk>',views.king  , name="king")
]
