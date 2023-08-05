from ...models.models import GymBranch
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
import json


class GymBranch_:
    @csrf_exempt
    def create(self, request) -> JsonResponse:
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        location = request.POST.get("location")
        open = request.POST.get("open")

        if name and phone and location and open:
            try:
                if GymBranch.objects.filter(location=location).exists():
                    return JsonResponse({"msg": "the location exists"})
                GymBranch.objects.create(
                    name=name, phone=phone, location=location, open=open
                )
                return JsonResponse({"msg": "success"})
            except IntegrityError:
                return JsonResponse({"msg": "it was not created"})
        else:
            return JsonResponse({"msg": "there are empty fields"})

    def getAll(self, request) -> JsonResponse:
        data = list(GymBranch.objects.all().values())
        return JsonResponse(data, safe=False)

    @csrf_exempt
    def update(self, request, id) -> JsonResponse:
        try:
            name = request.POST.get("name")
            phone = request.POST.get("phone")
            location = request.POST.get("location")
            open = request.POST.get("open")
            gymBranchFilter = GymBranch.objects.filter(id=id)
            if gymBranchFilter.exists():
                gymBranch = gymBranchFilter.get()
                gymBranch.name = name
                gymBranch.phone = phone
                gymBranch.location = location
                gymBranch.open = open
                gymBranch.save(update_fields=["phone", "name", "location", "open"])
                return JsonResponse({"put": True})
            else:
                return JsonResponse({"msg": False})
        except GymBranch.DoesNotExist:
            return JsonResponse({"msg": "nothing was found"})

    @csrf_exempt
    def delete(self, request, id) -> JsonResponse:
        if request.method == "DELETE":
            try:
                id = int(id)
                gymBranchFilter = GymBranch.objects.filter(id=id)
                if gymBranchFilter.exists():
                    gymBranch = gymBranchFilter.get()
                    gymBranch.delete()
                    return JsonResponse({"delete": True})
                else:
                    return JsonResponse({"delete": False})
            except GymBranch.DoesNotExist:
                return JsonResponse({"msg": "nothing was found"})
        else:
            return JsonResponse({"error": "Method not allowed"}, status=405)
