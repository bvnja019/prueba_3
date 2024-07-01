from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    return render (request, 'alumnos/index.html', context)

def quienesSomos(request):
    context = {}
    return render (request, 'alumnos/quienesSomos.html',context)