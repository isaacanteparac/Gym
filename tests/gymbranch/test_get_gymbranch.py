import pytest
from src.models.models import GymBranch
from src.controllers.gymBranch.GymBranch_ import GymBranch_
from django.test import RequestFactory

@pytest.fixture
def request_factory():
    return RequestFactory()

@pytest.fixture
def gym_branch_controller():
    return GymBranch_()


@pytest.mark.django_db
def test_get_all_gym_branches(request_factory, gym_branch_controller):
    GymBranch.objects.create(name="Gym A", phone="1234567890", location="Location A", open=True)
    GymBranch.objects.create(name="Gym B", phone="5555555555", location="Location B", open=True)
    GymBranch.objects.create(name="Gym C", phone="1111111111", location="Location C", open=True)

    request = request_factory.get("/get_all/")
    response = gym_branch_controller.getAll(request)

    assert response.status_code == 200
    data = response.content.decode("utf-8")
    assert isinstance(data, str)  
    assert "Gym A" in data
    assert "Gym B" in data
    assert "Gym C" in data

