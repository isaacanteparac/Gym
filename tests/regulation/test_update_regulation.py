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
def test_update_regulation(request_factory, regulation_controller):
    regulation = Regulation.objects.create(name="Test Regulation", code="test_code", description="Original description")

    request = request_factory.post(f"/update/{regulation.id}/", {
        "name": "Updated Regulation",
        "description": "Updated description"
    })
    response = regulation_controller.update(request, id=regulation.id)

    assert response.status_code == 200
    response_data = json.loads(response.content.decode('utf-8'))
    assert response_data == {"msg": True}
    updated_regulation = Regulation.objects.get(pk=regulation.id)
    assert updated_regulation.name == "Updated Regulation"
    assert updated_regulation.description == "Updated description"

@pytest.mark.django_db
def test_update_nonexistent_regulation(request_factory, regulation_controller):
    request = request_factory.post("/update/999/", {
        "name": "Updated Regulation",
        "description": "Updated description"
    })  # Use an invalid ID
    response = regulation_controller.update(request, id=999)

    assert response.status_code == 200
    response_data = json.loads(response.content.decode('utf-8'))
    assert response_data == {"msg": False}

@pytest.mark.django_db
def test_update_missing_fields(request_factory, regulation_controller):
    regulation = Regulation.objects.create(name="Test Regulation", code="test_code", description="Original description")

    request = request_factory.post(f"/update/{regulation.id}/", {
        "name": "Updated Regulation",
        "description": "Updated description"
    })
    response = regulation_controller.update(request, id=regulation.id)

    assert response.status_code == 200
    response_data = json.loads(response.content.decode('utf-8'))
    assert response_data == {"msg": True}
    updated_regulation = Regulation.objects.get(pk=regulation.id)
    assert updated_regulation.name == "Updated Regulation"
    assert updated_regulation.description == "Updated description"