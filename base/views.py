from django.shortcuts import render
from django.http import HttpResponse
from .models import rooms

# rooms =[
#     {'id' : 1 , 'name' : 'first id '},
#     {'id' : 2 , 'name' : 'second id '},
#     {'id' : 3 , 'name' : 'third id '},    
# ]
# Create your views here.
def home(request):
    context = {'rooms' : rooms}
    return render(request , 'base/home.html', context )



def king(request , pk):
    room = rooms.objects.get(id=pk)
    context = {'room' : room}   
    return render(request , 'base/king.html' , context )