import pytest
import json
from django.test import RequestFactory
from src.controllers.user.Assistance_ import Assistance_
from src.models.models import Assistance
from django.contrib.auth.models import User
from datetime import date

@pytest.fixture
def request_factory():
    return RequestFactory()

@pytest.fixture
def assistance_controller():
    return Assistance_()

@pytest.mark.django_db
def test_get_all_today(request_factory, assistance_controller):
    user = User.objects.create(username="test_user", is_superuser=False)
    assistance1 = Assistance.objects.create(idUser=user, date=date.today(), hour="12:00:00", state=True)
    assistance2 = Assistance.objects.create(idUser=user, date=date.today(), hour="14:00:00", state=False)
    request = request_factory.get("/get_all_today/")
    response = assistance_controller.getAllToday(request)
    assert response.status_code == 200
    response_data = json.loads(response.content.decode('utf-8'))
    assert len(response_data) == 2
    assert response_data[0]["id"] == assistance1.id
    assert response_data[1]["id"] == assistance2.id
