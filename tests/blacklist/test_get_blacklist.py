import json
import pytest
from django.test import RequestFactory
from src.controllers.regulation.BlackList_ import BlackList_
from src.models.models import Blacklist, Regulation
from django.contrib.auth.models import User

@pytest.fixture
def request_factory():
    return RequestFactory()

@pytest.fixture
def blacklist_controller():
    return BlackList_()

@pytest.mark.django_db
def test_get_all_blacklist(request_factory, blacklist_controller):
    user1 = User.objects.create(username="user1")
    user2 = User.objects.create(username="user2")
    regulation1 = Regulation.objects.create(code="regulation1")
    regulation2 = Regulation.objects.create(code="regulation2")
    Blacklist.objects.create(idUser=user1, idRegulation=regulation1, reason="Violation 1")
    Blacklist.objects.create(idUser=user2, idRegulation=regulation2, reason="Violation 2")
    request = request_factory.get("/get_all_blacklist/")
    response = blacklist_controller.getAll(request)
    assert response.status_code == 200
    response_data = json.loads(response.content.decode('utf-8'))
    expected_data = [
        {"idUser": user1.id, "idRegulation": regulation1.id, "reason": "Violation 1"},
        {"idUser": user2.id, "idRegulation": regulation2.id, "reason": "Violation 2"}
    ]

    for expected_item, response_item in zip(expected_data, response_data):
        assert expected_item["idUser"] == response_item["idUser"]
        assert expected_item["idRegulation"] == response_item["idRegulation"]
        assert expected_item["reason"] == response_item["reason"]
