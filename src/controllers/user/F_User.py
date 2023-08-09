from django.urls import path
from ...controllers.user.User_ import User_
from ...controllers.user.Assistance_ import Assistance_


class F_User:
    user = User_()
    assistance = Assistance_()

    def userEndpoints(self):
        return [
            path("api/users", self.user.getAll),
            path("api/user/create", self.user.create),
            path("api/user/auth", self.user.auth),
        ]

    def assistanceEndpoints(self):
        return [
            path("api/assitance/get", self.assistance.getAllToday),
            path("api/assitance/put/<id>", self.assistance.update),
            path("api/assitance/search", self.assistance.searchUser),
        ]
