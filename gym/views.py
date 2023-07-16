from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def login(request):
    return render(request, "components/register/login.html",)

def signup(request):
    return render(request, "components/register/signup.html")

@login_required
def signout(request):
    logout(request)
    return redirect("login")

@login_required
def client(request):

    return render(request, "components/client/main.html", {'user': request.user})

@login_required
def opetator(request):
    return render(request, "components/operator/main.html",)



#def signupAdmin(request):
#    return render(request, "components/register/signup.html", {"admin": True})


