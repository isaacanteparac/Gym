from django.urls import path
from ...controllers.regulation.Regulation_ import Regulation_
from ...controllers.regulation.BlackList_ import BlackList_


class F_Regulation:
    blackList = BlackList_()
    regulation = Regulation_()

    def blackListEndpoints(self):
        return [
            path("api/blacklist/create", self.blackList.create),
            path("api/blacklist/get/all", self.blackList.getAll),
            path("api/blacklist/delete/<id>", self.blackList.delete),
        ]

    def regulationEndpoints(self):
        return [
            path("api/regulation/create", self.regulation.create),
            path("api/regulation/get/all", self.regulation.getAll),
            path("api/regulation/put/<id>", self.regulation.update),
            path("api/regulation/delete/<id>", self.regulation.delete),
        ]
