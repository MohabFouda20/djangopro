from django.shortcuts import render
from django.http import HttpResponse
rooms =[
    {'id' : 1 , 'name' : 'first id '},
    {'id' : 2 , 'name' : 'second id '},
    {'id' : 3 , 'name' : 'third id '},    
]
# Create your views here.
def home(request):
    context = {'rooms' : rooms}
    return render(request , 'base/home.html', context )



def king(request , pk):
    kingg = None 
    for i in rooms :
        if i['id'] == int(pk):
            kingg = i 
            break
    if kingg is None :
        return HttpResponse("not availaible")
    context = {'kingg' : kingg}   
    return render(request , 'base/king.html' , context )