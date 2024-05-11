from django.shortcuts import render, HttpResponse



# Create your views here.
def order(request):
    context = {
        "this_is_var" : "this is embeded variable "
    }
    return render(request,"cakesites/order.html")
def order(request):
    context = {
        "this_is_var" : "this is embeded variable "
    }
    return render(request,"cakesites/order.html",context)


