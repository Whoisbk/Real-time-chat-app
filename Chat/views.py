from django.shortcuts import render

# Create your views here.


def main(request):
    
    return render(request,'Chat/main.html')


def lobby(request,lobby_name):

    context = {'lobby_name':lobby_name}
    return render(request,'Chat/lobby.html',context)
