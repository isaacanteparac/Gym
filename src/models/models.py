from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Assistance(models.Model):
    state = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)
    hour = models.TimeField(default=timezone.now)
    idUser = models.ForeignKey(User, on_delete=models.CASCADE)

    def convertTojson(self):
        return {
            "id": self.id,
            "state": self.state,
            "date": self.date,
            "hour": self.hour,
            "idUser": self.idUser.id,
            "username": self.idUser.username,
            "first_name": self.idUser.first_name,
            "last_name":self.idUser.last_name,
        }

    def __str__(self) -> str:
        view = f"ID: {self.id} | STATE: {self.state} | DATE: {self.date} | HOUE: {self.hour} | ID_USER: {self.idUser.id}"
        return view


class Regulation(models.Model):
    name = models.CharField(max_length=50)  # Nombre del reglamento
    code = models.CharField(max_length=5)
    description = models.TextField()  # Descripción del reglamento

    def __str__(self):
        return f"ID:{self.id} | NAME: {self.name} | DESCRIPTION: {self.description} | CODE: {self.code}"


class Blacklist(models.Model):
    idUser = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="blacklist"
    )  # Relación uno a uno con el modelo User
    id_reglamento = models.ForeignKey(
        "Regulation", on_delete=models.CASCADE
    )  # Relación con el modelo Reglamento
    reason = models.TextField()  # Motivo de inclusión en la lista negra
    date = models.DateTimeField(
        auto_now_add=True
    )  # Fecha y hora en que se agregó a la lista negra

    def __str__(self):
        return f"ID: {self.id} | IDUSER: {self.idUser.username} | REASON: {self.reason} | DATE: {self.date_added}"


class GymBranch(models.Model):
    name = models.CharField(max_length=200)  # Nombre de la sucursal
    phone = models.CharField(max_length=20)  # Teléfono de la sucursal
    location = models.CharField(max_length=200)  # Dirección de la sucursal
    open = models.BooleanField(default=True)  # si se encuentra abierto on no

    def __str__(self):
        return f"ID: {self.id} | Nombre: {self.nombre} | Teléfono: {self.telefono} | Dirección: {self.direccion}"
