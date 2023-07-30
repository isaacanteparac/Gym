from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

def register(request):
    return render(request, "register.html",)

@login_required
def signout(request):
    logout(request)
    return redirect("login")

@login_required
def client(request):
    return render(request, "client.html", {'user': request.user})

@login_required
def opetator(request):
    return render(request, "operator.html",)

