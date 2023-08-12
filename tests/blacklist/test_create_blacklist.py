import pytest
from django.test import RequestFactory
from src.controllers.regulation.BlackList_ import BlackList_
from src.models.models import Regulation
from django.contrib.auth.models import User
import json

@pytest.fixture
def request_factory():
    return RequestFactory()

@pytest.fixture
def blacklist_controller():
    return BlackList_()

@pytest.mark.django_db
def test_create_blacklist(request_factory, blacklist_controller):
    user = User.objects.create(username="test_user")
    regulation = Regulation.objects.create(code="test_code")

    request = request_factory.post("/create_blacklist/", {
        "codeRegulation": "test_code",
        "username": "test_user",
        "reason": "Violation"
    })
    response = blacklist_controller.create(request)

    assert response.status_code == 200
    response_data = json.loads(response.content.decode('utf-8'))
    assert response_data == {"msg": "created successfully"}