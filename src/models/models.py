from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class GymBranch(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=200)
    open = models.BooleanField(default=True)

    def __str__(self):
        return f"ID: {self.id} | Nombre: {self.nombre} | Teléfono: {self.telefono} | Dirección: {self.direccion}"


class Assistance(models.Model):
    state = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)
    hour = models.TimeField(default=timezone.now)
    idUser = models.ForeignKey(User, on_delete=models.CASCADE)
    idBranch = models.ForeignKey(GymBranch, on_delete=models.CASCADE, null=True, blank=True)

    def convertTojson(self):
        return {
            "id": self.id,
            "state": self.state,
            "date": self.date,
            "hour": self.hour,
            "idUser": self.idUser.id,
            "username": self.idUser.username,
            "first_name": self.idUser.first_name,
            "last_name": self.idUser.last_name,
        }

    def __str__(self) -> str:
        view = f"ID: {self.id} | STATE: {self.state} | DATE: {self.date} | HOUE: {self.hour} | ID_USER: {self.idUser.id}"
        return view


class Regulation(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=5)
    description = models.TextField()

    def __str__(self):
        return f"ID:{self.id} | NAME: {self.name} | DESCRIPTION: {self.description} | CODE: {self.code}"


class Blacklist(models.Model):
    idUser = models.ForeignKey(User, on_delete=models.CASCADE)
    idRegulation = models.ForeignKey(Regulation, on_delete=models.CASCADE)
    reason = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def convertTojson(self):
        return {
            "id": self.id,
            "reason": self.reason,
            "codeRegulation": self.idRegulation.code,
            "username": self.idUser.username,
            "userActive": self.idUser.is_active,
            "first_name": self.idUser.first_name,
            "last_name": self.idUser.last_name,
        }

    def __str__(self):
        return f"ID: {self.id} | IDUSER: {self.idUser.username} | REASON: {self.reason} | DATE: {self.date_added}"