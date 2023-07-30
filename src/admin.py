from django.contrib import admin
from .models.models import Assistance, GymBranch, Regulation, Blacklist

# Register your models here.
admin.site.register(Assistance)
admin.site.register(GymBranch)
admin.site.register(Regulation)
admin.site.register(Blacklist)
