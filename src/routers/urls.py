from django.urls import path
from . import views
from ..controllers.gymBranch.GymBranch_ import GymBranch_
from ..controllers.user.F_User import F_User
from ..controllers.regulation.F_Regulation import F_Regulation

fuser = F_User()
fregulation = F_Regulation()
gymBranch = GymBranch_()

urlpatterns = [
    path("", views.login, name="login"),
    path("sign-up/", views.signup, name="signup"),
    path("logout/", views.signout, name="logout"),
    path("profile/", views.client, name="clientMain"),
    path("operator/", views.opetator, name="operatorMain"),    

    #gymbranch
    path("api/branch/get", gymBranch.getAll),
    path("api/branch/create", gymBranch.create),
    path("api/branch/put/<id>", gymBranch.update),
    path("api/branch/delete/<id>", gymBranch.delete),

]

urlpatterns.extend(fuser.userEndpoints())
urlpatterns.extend(fuser.assistanceEndpoints())
urlpatterns.extend(fregulation.regulationEndpoints())
urlpatterns.extend(fregulation.blackListEndpoints())
