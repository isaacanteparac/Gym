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
def test_delete_existing_regulation(request_factory, regulation_controller):
    regulation = Regulation.objects.create(name="Test Regulation", code="test_code", description="Original description")
    request = request_factory.delete(f"/delete/{regulation.id}/")
    response = regulation_controller.delete(request, id=regulation.id)
    assert response.status_code == 200
    response_data = json.loads(response.content.decode('utf-8'))
    assert response_data == {"msg": True}
    with pytest.raises(Regulation.DoesNotExist):
        Regulation.objects.get(pk=regulation.id)

@pytest.mark.django_db
def test_delete_nonexistent_regulation(request_factory, regulation_controller):
    request = request_factory.delete("/delete/999/")
    response = regulation_controller.delete(request, id=999)

    assert response.status_code == 200
    response_data = json.loads(response.content.decode('utf-8'))
    assert response_data == {"msg": False}
