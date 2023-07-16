from django.urls import path
from . import views
from .src.user.Users import Users

user = Users()

urlpatterns = [
    path("", views.login, name="login"),
    path("sign-up/", views.signup, name="signup"),
    path("logout/", views.signout, name="logout"),

    path("profile/", views.client, name="clientMain"),
    path("operator/", views.opetator, name="operatorMain"),


    #api
    path("api/users", user.getAll),
    path("api/user/create", user.create),
    path("api/user/auth", user.auth),
]
