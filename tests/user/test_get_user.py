import json
import pytest
from django.contrib.auth.models import User
from src.controllers.user.User_ import User_
from django.test import RequestFactory

@pytest.fixture
def user_instance():
    return User_()

@pytest.mark.django_db
def test_get_all_users(user_instance):
    num_users = 5
    for i in range(num_users):
        username = f"testuser_{i}"
        password = f"testpassword_{i}"
        User.objects.create_user(username=username, password=password)

    request_factory = RequestFactory()
    request = request_factory.get('/api/users')
    user_controller = user_instance
    response = user_controller.getAll(request)
    assert response.status_code == 200
    users_all = json.loads(response.content)
    assert len(users_all) == num_users
