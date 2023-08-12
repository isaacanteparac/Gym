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
def test_update_existing_gym_branch(request_factory, gym_branch_controller):
    gym_branch = GymBranch.objects.create(name="Gym A", phone="1234567890", location="Location A", open=True)
    updated_data = {
        "name": "Updated Gym A",
        "phone": "5555555555",
        "location": "Updated Location A",
        "open": False,
    }

    request = request_factory.post(f"/update/{gym_branch.id}/", updated_data)
    response = gym_branch_controller.update(request, id=gym_branch.id)

    assert response.status_code == 200
    assert response.content.decode("utf-8") == '{"msg": true}'
    updated_branch = GymBranch.objects.get(id=gym_branch.id)
    assert updated_branch.name == updated_data["name"]
    assert updated_branch.phone == updated_data["phone"]
    assert updated_branch.location == updated_data["location"]
    assert updated_branch.open == updated_data["open"]

@pytest.mark.django_db
def test_update_nonexistent_gym_branch(request_factory, gym_branch_controller):
    request = request_factory.post("/update/999/", {})
    response = gym_branch_controller.update(request, id=999)

    assert response.status_code == 200
    assert response.content.decode("utf-8") == '{"msg": false}'

@pytest.mark.django_db
def test_update_exception(request_factory, gym_branch_controller):
    try:
        request = request_factory.post("/update/999/", {})
        gym_branch_controller.update(request, id=999)
    except GymBranch.DoesNotExist:
        pass