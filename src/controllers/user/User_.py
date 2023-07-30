from django.shortcuts import redirect
from django.http import JsonResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt


class User_:
    name = ""
    last_name = ""
    email = ""
    password = ""
    admin = False

    ui = {
        "client": "clientMain",
        "operator": "operatorMain",
        "r_login": "../templates/components/register/login.html",
        "r_signup": "../templates/components/register/signup.html",
    }

    msg = {
        "error": {"user": "Email o Usuario ya se encuentran registrados"},
        "success": {
            "user": "Usuario existe",
        },
    }

    @csrf_exempt
    def auth(self, request) -> None:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_superuser:
                    renderHtml = self.ui["operator"]
                else:
                    renderHtml = self.ui["client"]
                return redirect(renderHtml)
            else:
                return redirect("login")

    @csrf_exempt
    def create(self, request) -> None:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        passwordRepeat = request.POST.get("passwordRepeat")

        if not (
            first_name != ""
            and last_name != ""
            and email != ""
            and username != ""
            and password != ""
            and passwordRepeat != ""
        ):
            if (password == passwordRepeat) and (
                not User.objects.filter(username=username).exists()
                and not User.objects.filter(email=email).exists()
            ):
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
                    return redirect("login")
            else:
                return redirect("login")
        else:
            return redirect("login")

    @csrf_exempt
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

    @csrf_exempt
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

    @csrf_exempt
    def searchUsername(self, request, username) -> JsonResponse:
        user = list(User.objects.filter(username=username).values())
        return JsonResponse(user, safe=False)

    def getAllNoAdmin(self, request) -> JsonResponse:
        user = list(User.objects.filter(is_superuser=0).values())
        return JsonResponse(user, safe=False)

    def getAllAdmin(self, request) -> JsonResponse:
        user = list(User.objects.filter(is_superuser=1).values())
        return JsonResponse(user, safe=False)
