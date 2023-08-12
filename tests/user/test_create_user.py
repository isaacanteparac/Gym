import pytest
from django.test import RequestFactory
from django.contrib.auth.models import User
from unittest.mock import patch
from src.controllers.user.User_ import User_

@pytest.fixture
def user_instance():
    return User_()

@pytest.mark.django_db
@patch("src.controllers.user.User_.login")
@patch("src.controllers.user.User_.User.objects.create_user")
def test_create_successful(mock_create_user, mock_login, user_instance):
    factory = RequestFactory()
    request = factory.post('/fake-url/', {
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'john@example.com',
        'username': 'johndoe',
        'password': 'password123',
        'passwordRepeat': 'password123',
    })

    mock_create_user.return_value = User()
    response = user_instance.create(request)

    assert response.status_code == 302
    assert response.url in ["/profile/"]
    mock_create_user.assert_called_once_with(
        first_name='John',
        last_name='Doe',
        email='john@example.com',
        username='johndoe',
        password='password123'
    )
    mock_login.assert_called_once_with(request, mock_create_user.return_value)

def test_create_password_mismatch(user_instance):
    factory = RequestFactory()
    request = factory.post('/fake-url/', {
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'john@example.com',
        'username': 'johndoe',
        'password': 'password123',
        'passwordRepeat': 'differentpassword',
    })

    response = user_instance.create(request)

    assert response.status_code == 302
    assert response.url in ["/sign-up/"]
