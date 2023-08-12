import pytest
from django.test import RequestFactory
from django.contrib.auth.models import User
from django.contrib.sessions.middleware import SessionMiddleware
from src.controllers.user.User_ import User_

@pytest.fixture
def user_instance():
    return User_()

@pytest.fixture
def mock_authenticated_user():
    return User.objects.create_user(username='testuser', password='testpassword')

@pytest.mark.django_db
def test_auth_successful(user_instance, mock_authenticated_user):
    factory = RequestFactory()
    request = factory.post('/fake-url/', {'username': 'testuser', 'password': 'testpassword'})
    request.user = mock_authenticated_user

    middleware = SessionMiddleware(lambda request: None)
    middleware.process_request(request)

    response = user_instance.auth(request)

    assert response.status_code == 302  # Asegúrate de que este sea el estado correcto
    assert response.url in ['/profile/', '/operator/']  # Asegúrate de que esta sea una de las URLs