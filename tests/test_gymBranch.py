import pytest
from django.db.utils import IntegrityError
from src.models.models import GymBranch
from src.controllers.gymBranch.GymBranch_ import GymBranch_  # Ajusta la importación según tu estructura
from django.test import RequestFactory

@pytest.fixture
def request_factory():
    return RequestFactory()

@pytest.fixture
def gym_branch_controller():
    return GymBranch_()  # Crea una instancia de tu controlador

@pytest.mark.django_db
def test_create_successful(request_factory, gym_branch_controller):
    data = {
        "name": "Gym A",
        "phone": "1234567890",
        "location": "Location A",
        "open": True,
    }
    request = request_factory.post("/create/", data)
    response = gym_branch_controller.create(request)

    assert response.status_code == 200
    assert GymBranch.objects.filter(name=data["name"]).exists()

@pytest.mark.django_db
def test_create_existing_location(request_factory, gym_branch_controller):
    GymBranch.objects.create(name="Existing Gym", phone="987-654-3210", location="Location B", open=True)

    data = {
        "name": "Gym B",
        "phone": "5555555555",
        "location": "Location B",
        "open": True,
    }
    request = request_factory.post("/create/", data)
    response = gym_branch_controller.create(request)

    assert response.status_code == 200
    assert response.content.decode("utf-8") == '{"msg": "the location exists"}'
    assert not GymBranch.objects.filter(name=data["name"]).exists()

@pytest.mark.django_db
def test_create_empty_fields(request_factory, gym_branch_controller):
    data = {
        "name": "Gym C",
        "phone": "1111111111",
        # Faltan campos obligatorios
    }
    request = request_factory.post("/create/", data)
    response = gym_branch_controller.create(request)

    assert response.status_code == 200
    assert response.content.decode("utf-8") == '{"msg": "there are empty fields"}'
    assert not GymBranch.objects.filter(name=data["name"]).exists()
