from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html")
def about(request):
    return HttpResponse("this is about me ")

def cakes(request):
    return HttpResponse("cakes here")

# def order(request):
#     return HttpResponse("cakes order")
