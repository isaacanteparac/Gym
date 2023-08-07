from django.urls import path
from . import views
from ..controllers.user.User_ import User_
from ..controllers.user.Assistance_ import Assistance_
from ..controllers.gymBranch.GymBranch_ import GymBranch_
from ..controllers.regulation.Regulation_ import Regulation_
from ..controllers.regulation.BlackList_ import BlackList_


user = User_()
assistance = Assistance_()
gymBranch = GymBranch_()
regulation = Regulation_()
blackList = BlackList_()

urlpatterns = [
    path("", views.register, name="login"),
    path("logout/", views.signout, name="logout"),
    path("profile/", views.client, name="clientMain"),
    path("operator/", views.opetator, name="operatorMain"),    

    #api
    path("api/users", user.getAll),
    path("api/user/create", user.create),
    path("api/user/auth", user.auth),

    #asistencia
    path("api/assitance/get", assistance.getAllToday),
    path("api/assitance/put/<id>", assistance.update),
    path("api/assitance/search", assistance.searchUser),

    #gymbranch
    path("api/branch/get", gymBranch.getAll),
    path("api/branch/create", gymBranch.create),
    path("api/branch/put/<id>", gymBranch.update),
    path("api/branch/delete/<id>", gymBranch.delete),


    #regulations
    path("api/regulation/create", regulation.create),
    path("api/regulation/get/all", regulation.getAll),
    path("api/regulation/put/<id>", regulation.update),
    path("api/regulation/delete/<id>", regulation.delete),

    #blacklist
    path("api/blacklist/create", blackList.create),
    path("api/blacklist/get/all", blackList.getAll),
    path("api/blacklist/delete/<id>", blackList.delete),

]
