from django.contrib.auth.models import User
from ...models.models import Assistance
from django.http import JsonResponse, HttpResponse
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
        takeAttendance = threading.Timer(hours_delay, self.assistanceAutomatically)
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
    def searchUser(self, request) -> JsonResponse:
        try:
            usernameResearch = request.POST.get("searcher")
            date_ = date.today()
            userFilter = User.objects.filter(username=usernameResearch)
            if userFilter.exists():
                user = userFilter.get()
                userAssistanceSearch = Assistance.objects.filter(idUser=user.id, date=date_)
                if userAssistanceSearch.exists():
                    userAssistance = userAssistanceSearch.get()
                    data = {
                        "first_name": user.first_name,
                        "last_name": user.last_name,
                        "username": user.username,
                        "date": userAssistance.date,
                        "state": userAssistance.state
                    }
                    return JsonResponse({"success": True, "data":data})
                else:
                    return JsonResponse({"success":False})
        except User.DoesNotExist:
            return JsonResponse({"success":False})
        

    @csrf_exempt
    def update(self, request,id) ->JsonResponse:
        try:
            state = request.POST.get("state")
            assistenceFilter = Assistance.objects.filter(id=id)
            if assistenceFilter.exists():
                assistance = assistenceFilter.get()
                assistance.hour = timezone.localtime().time()
                assistance.state = state
                assistance.save(update_fields=['hour','state'])
                return JsonResponse({"put":True})
            else:
                return JsonResponse({"msg": False})
        except Assistance.DoesNotExist:
            return JsonResponse({"msg": "no se encontro nada"})
        


