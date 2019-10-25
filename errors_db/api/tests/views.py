import pytest
from django.urls import reverse

from errors_db.api.models import ErrorInstance, Solution, Situation


@pytest.mark.django_db
def test_user_view(client):
    response = client.get(reverse("user"))

    assert response.status_code == 200
    assert response.json()["username"].endswith("@example.com")


@pytest.mark.django_db
class TestErrorInstanceViewSet:
    @pytest.fixture
    def create_solution(self):
        def _create_solution(type, text, situation=None):
            Solution.objects.create(solution_type=type, text=text, situation=situation)

        return _create_solution

    @pytest.fixture
    def create_situation(self):
        def _create_situation(error_msg, context):
            Situation.objects.create(error_msg=error_msg, context=context)

        return _create_situation

    def test_create(self, client, create_solution):
        error_data = {
            "message": "Test Message",
            "context": {},
            "stacktrace": "test stacktrace",
        }

        create_solution(0, "Please visit this doc: http://help.salesforce.com/")
        create_solution(1, "Please retry the operation.")

        response = client.post(
            reverse("errorinstance-list"), data=error_data, format="json"
        )

        expected_data = {"solutions": "No solutions found."}
        assert response.data == expected_data
        assert response.status_code == 201
