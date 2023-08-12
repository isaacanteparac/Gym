import pytest
import json
from django.test import RequestFactory
from src.controllers.regulation.BlackList_ import BlackList_
from src.models.models import Blacklist, Regulation
from django.contrib.auth.models import User


blacklist_controller = BlackList_()

@pytest.mark.django_db
def test_delete_blacklist():
    request_factory = RequestFactory()
    user = User.objects.create(username="test_user")
    regulation = Regulation.objects.create(code="test_code")
    blacklist_entry = Blacklist.objects.create(idUser=user, idRegulation=regulation, reason="Violation")
    request = request_factory.delete(f"/delete_blacklist/{blacklist_entry.id}/")
    response = blacklist_controller.delete(request, id=blacklist_entry.id)
    assert response.status_code == 200
    response_data = json.loads(response.content.decode('utf-8'))
    assert response_data == {"delete": True}

    # Verificar que el usuario esté activo nuevamente
    user.refresh_from_db()
    assert user.is_active == True

    with pytest.raises(Blacklist.DoesNotExist):
        blacklist_entry.refresh_from_db()
