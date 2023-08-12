import pytest
import json
from django.test import RequestFactory
from src.controllers.user.Assistance_ import Assistance_
from src.models.models import Assistance, GymBranch
from django.contrib.auth.models import User

@pytest.fixture
def request_factory():
    return RequestFactory()

@pytest.fixture
def assistance_controller():
    return Assistance_()

@pytest.mark.django_db
def test_update_existing_assistance(request_factory, assistance_controller):
    user = User.objects.create(username="test_user", is_superuser=False)
    assistance = Assistance.objects.create(idUser=user, date="2023-08-11", hour="12:00:00", state=True)
    gym_branch = GymBranch.objects.create(id=1, name="Gym 1")
    request = request_factory.post(f"/update/{assistance.id}/", {"state": False, "idBranch": 1})
    response = assistance_controller.update(request, id=assistance.id)

    assert response.status_code == 200
    response_data = json.loads(response.content.decode('utf-8'))
    assert response_data == {"put": True}

    updated_assistance = Assistance.objects.get(pk=assistance.id)
    assert updated_assistance.state == False
    assert updated_assistance.idBranch == gym_branch

@pytest.mark.django_db
def test_update_nonexistent_assistance(request_factory, assistance_controller):
    request = request_factory.post("/update/999/", {"state": False, "idBranch": 1})  # Use an invalid ID
    response = assistance_controller.update(request, id=999)

    assert response.status_code == 200
    response_data = json.loads(response.content.decode('utf-8'))
    assert response_data == {"msg": False, "idb": "1"}