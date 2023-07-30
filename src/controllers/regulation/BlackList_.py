from ...models.models import Blacklist, Regulation
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError


class BlackList_:
    date = None

    @csrf_exempt
    def create(self, request) -> JsonResponse:
        codeRegulation = request.POST.get("codeRegulation")
        username = request.POST.get("username")
        reason = request.POST.get("reason")

        if codeRegulation and username and reason:
            try:
                regulationFilter = Regulation.objects.filter(code=codeRegulation)
                userFilter = User.objects.filter(username=username)
                if regulationFilter.exists() and userFilter.exists():
                    regulation = regulationFilter.get()
                    user = userFilter.get()
                    Blacklist.objects.create(
                        idUser=user,
                        idRegulation=regulation,
                        reason=reason,
                    )
                    user.is_active = False
                    user.save(update_fields=["is_active"])
                    return JsonResponse({"msg": "success"})
            except Regulation.DoesNotExist:
                return JsonResponse({"msg": "there is no regulation"})
            except User.DoesNotExist:
                return JsonResponse({"msg": "no user exists"})
        else:
            return JsonResponse({"msg": "there are empty fields"})

    def getAll(self, request) -> JsonResponse:
        blacklist = Blacklist.objects.all()
        data = [bl.convertTojson() for bl in blacklist]
        return JsonResponse(data, safe=False)

    @csrf_exempt
    def delete(self, request, id) -> JsonResponse:
        if request.method == "DELETE":
            try:
                id = int(id)
                blacklistFilter = Blacklist.objects.filter(id=id)
                if blacklistFilter.exists():
                    regulation = blacklistFilter.get()
                    m = regulation.idUser.id
                    userState = User.objects.get(id=m)
                    userState.is_active = True
                    userState.save(update_fields=["is_active"])
                    regulation.delete()
                    return JsonResponse({"delete": True})
                else:
                    return JsonResponse({"delete": False})
            except blacklistFilter.DoesNotExist:
                return JsonResponse({"msg": "no se encontro nada"})
        else:
            return JsonResponse({"error": "Method not allowed"}, status=405)
