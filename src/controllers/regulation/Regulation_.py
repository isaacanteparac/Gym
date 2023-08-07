from ...models.models import Regulation
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError


class Regulation_:
    date = None

    @csrf_exempt
    def create(self, request) -> JsonResponse:
        name = request.POST.get("name")
        code = request.POST.get("code")
        description = request.POST.get("description")

        if name and code and description:
            try:
                if Regulation.objects.filter(code=code).exists():
                    return JsonResponse({"msg": "the code exists"})
                Regulation.objects.create(
                    name=name,
                    code=code,
                    description=description,
                )
                return JsonResponse({"msg": "success"})
            except IntegrityError:
                return JsonResponse({"msg": "it was not created"})
        else:
            return JsonResponse({"msg": "there are empty fields"})

    def getAll(self, request) -> JsonResponse:
        data = list(Regulation.objects.all().values())
        return JsonResponse(data, safe=False)

    
    @csrf_exempt
    def update(self, request, id) -> JsonResponse:
        try:
            description = request.POST.get("description")
            name = request.POST.get("name")
            regulationFilter = Regulation.objects.filter(id=id)
            if regulationFilter.exists():
                regulation = regulationFilter.get()
                regulation.description = description
                regulation.name = name
                regulation.save(update_fields=["description","name"])
                return JsonResponse({"put": True})
            else:
                return JsonResponse({"msg": False})
        except Regulation.DoesNotExist:
            return JsonResponse({"msg": "no se encontro nada"})

    @csrf_exempt
    def delete(self, request, id) -> JsonResponse:
        if request.method == "DELETE":
            try:
                id = int(id)
                regulationFilter = Regulation.objects.filter(id=id)
                if regulationFilter.exists():
                    regulation = regulationFilter.get()
                    regulation.delete()
                    return JsonResponse({"delete": True})
                else:
                    return JsonResponse({"delete": False})
            except Regulation.DoesNotExist:
                return JsonResponse({"msg": "nothing was found"})
        else:
            return JsonResponse({"error": "Method not allowed"}, status=405)