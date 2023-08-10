from django.contrib.auth.models import User
from ...models.models import Assistance, GymBranch
from django.http import JsonResponse
import threading
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from datetime import date


class Assistance_:
    state = False
    date = None
    idUser = None

    def __init__(self) -> None:
        hours_delay = 24 * 3600
        takeAttendance = threading.Timer(3, self.assistanceAutomatically)
        takeAttendance.start()

    def assistanceAutomatically(self) -> None:
        users = list(User.objects.all())
        for user in users:
            self.create(user)

    def create(self, user) -> JsonResponse:
        try:
            Assistance.objects.create(idUser=user)
            return JsonResponse({"msg": "success"})
        except User.DoesNotExist:
            return JsonResponse({"msg": "error"})

    def getAllToday(self, request) -> JsonResponse:
        date_ = date.today()
        assistances = Assistance.objects.filter(date=date_)
        data = [assistance.convertTojson() for assistance in assistances]
        return JsonResponse(data, safe=False)

    @csrf_exempt
    def update(self, request, id) -> JsonResponse:
        try:
            state = request.POST.get("state")
            idBranch = request.POST.get("idBranch")
            assistenceFilter = Assistance.objects.filter(id=id)
            gymBranchFilter = GymBranch.objects.filter(id=idBranch)
            if assistenceFilter.exists():
                assistance = assistenceFilter.get()
                gymBranch = gymBranchFilter.get()
                assistance.hour = timezone.localtime().time()
                assistance.state = state
                if gymBranchFilter.exists():
                    assistance.idBranch = gymBranch
                    assistance.save(update_fields=["idBranch"])

                assistance.save(update_fields=["hour", "state"])
                return JsonResponse({"put": True})
            else:
                return JsonResponse({"msg": False, "idb": idBranch})
        except Assistance.DoesNotExist:
            return JsonResponse({"msg": "no se encontro nada"})
        except GymBranch.DoesNotExist:
            return JsonResponse({"msg": "no se encontro nada"})
