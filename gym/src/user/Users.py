from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User


class Users:
    name = ""
    last_name = ""
    email = ""
    password = ""
    admin = False

    def auth(self, request) -> None:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("clientMain")
            else:
                return render(
                    request,
                    "../templates/components/register/login.html",
                    {"error": "Contraseña o Email incorrecto", "active": True},
                )

            """try:
                user = Users.objects.get(email=email)
            except User.DoesNotExist:
                user = None
            if user is not None and check_password(password, user.password):
                print("todo correcto")
                print(user)
                login(request, user)
                return redirect("clientMain")
            else:
                return render(
                    request,
                    "../templates/components/register/login.html",
                    {"error": "Contraseña o Email incorrecto", "active": True},
                )"""
        # return redirect("login")

    def create(self, request) -> None:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        passwordRepeat = request.POST.get("passwordRepeat")
        if password == passwordRepeat:
            try:
                user = User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    username=username,
                    password=password,
                )
                user.save()
                login(request, user)
                return redirect("clientMain")
            except InterruptedError:
                return render("signup", {"msg": "Usuario existe"})

        return redirect("signup")

    def update(self, request, username) -> JsonResponse:
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return JsonResponse({"update": False})
        user.first_name = request.POST.get("name")
        user.last_name = request.POST.get("last_name")
        user.password = request.POST.get("password")
        user.save()
        return JsonResponse({"update": True})

    def delete(self, request, username) -> JsonResponse:
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return JsonResponse({"delete": False})
        user.delete()
        return JsonResponse({"delete": True})

    def getAll(self, request) -> JsonResponse:
        usersAll = list(User.objects.values())
        return JsonResponse(usersAll, safe=False)

    def searchUsername(self, request, username) -> JsonResponse:
        user = list(User.objects.filter(username=username).values())
        return JsonResponse(user, safe=False)

    def getAllNoAdmin(self, request) -> JsonResponse:
        user = list(User.objects.filter(is_superuser=0).values())
        return JsonResponse(user, safe=False)

    def getAllAdmin(self, request) -> JsonResponse:
        user = list(User.objects.filter(is_superuser=1).values())
        return JsonResponse(user, safe=False)
