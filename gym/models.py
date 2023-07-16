from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Assistance(models.Model):
    state = models.BooleanField(default=False)
    day = models.DateField()
    idUser = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        view = f"ID:{self.id} | STATE: {self.state} | DAY: {self.day} | IDUSER: {self.idUser.dni}"
        return view

class Coach(models.Model):
    specialty = models.CharField(max_length=200)
    start_hours = models.TimeField()
    final_hours = models.TimeField()
    day = models.CharField(max_length=200)
    available = models.BooleanField(default=True)
    idUser = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        view = f"ID:{self.id} | SPECIALTY: {self.specialty} | AVALIBLE: {self.available} | DNI: {self.idUser.dni}"
        return view

