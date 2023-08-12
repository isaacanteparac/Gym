import pytest
import json
from django.test import RequestFactory
from src.controllers.regulation.Regulation_ import Regulation_
from src.models.models import Regulation

@pytest.fixture
def request_factory():
    return RequestFactory()

@pytest.fixture
def regulation_controller():
    return Regulation_()

@pytest.mark.django_db
def test_create_regulation(request_factory, regulation_controller):
    request = request_factory.post("/create/", {
        "name": "Test Regulation",
        "code": "test_code",
        "description": "This is a test regulation"
    })
    response = regulation_controller.create(request)
    assert response.status_code == 200
    response_data = json.loads(response.content.decode('utf-8'))
    assert response_data == {"msg": "the regulation was created correctly"}
    assert Regulation.objects.filter(code="test_code").exists()

@pytest.mark.django_db
def test_create_existing_code(request_factory, regulation_controller):
    Regulation.objects.create(name="Existing Regulation", code="existing_code", description="Existing description")

    request = request_factory.post("/create/", {
        "name": "Test Regulation",
        "code": "existing_code",
        "description": "This is a test regulation"
    })
    response = regulation_controller.create(request)

    assert response.status_code == 200
    response_data = json.loads(response.content.decode('utf-8'))
    assert response_data == {"msg": "the code exists"}

@pytest.mark.django_db
def test_create_missing_fields(request_factory, regulation_controller):
    request = request_factory.post("/create/", {
        "name": "Test Regulation",
        "description": "This is a test regulation"
    })
    response = regulation_controller.create(request)

    assert response.status_code == 200
    response_data = json.loads(response.content.decode('utf-8'))
    assert response_data == {"msg": "there are empty fields"}

@pytest.mark.django_db
def test_get_all_regulations(request_factory, regulation_controller):
    Regulation.objects.create(name="Regulation 1", code="code1", description="Description 1")
    Regulation.objects.create(name="Regulation 2", code="code2", description="Description 2")

    request = request_factory.get("/get_all/")
    response = regulation_controller.getAll(request)

    assert response.status_code == 200
    response_data = json.loads(response.content.decode('utf-8'))
    assert len(response_data) == 2
    assert response_data[0]["code"] == "code1"
    assert response_data[1]["code"] == "code2"
