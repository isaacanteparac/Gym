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
def test_delete_existing_gym_branch(request_factory, gym_branch_controller):
    gym_branch = GymBranch.objects.create(name="Gym A", phone="1234567890", location="Location A", open=True)

    request = request_factory.delete(f"/delete/{gym_branch.id}/")
    response = gym_branch_controller.delete(request, id=gym_branch.id)

    assert response.status_code == 200
    assert response.content.decode("utf-8") == '{"msg": true}'
    assert not GymBranch.objects.filter(id=gym_branch.id).exists()

@pytest.mark.django_db
def test_delete_nonexistent_gym_branch(request_factory, gym_branch_controller):
    request = request_factory.delete("/delete/999/")
    response = gym_branch_controller.delete(request, id=999)

    assert response.status_code == 200
    assert response.content.decode("utf-8") == '{"msg": false}'

@pytest.mark.django_db
def test_delete_exception(request_factory, gym_branch_controller):
    try:
        request = request_factory.delete("/delete/999/")
        gym_branch_controller.delete(request, id=999)
    except GymBranch.DoesNotExist:
        pass

def test_delete_invalid_method(request_factory, gym_branch_controller):
    request = request_factory.get("/delete/1/")
    response = gym_branch_controller.delete(request, id=1)

    assert response.status_code == 405
    assert response.content.decode("utf-8") == '{"error": "Method not allowed"}'