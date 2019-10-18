import pytest
from freezegun import freeze_time
from datetime import datetime, timezone

from errors_db.api.models import ErrorInstance, Situation, Solution

TEST_ERROR_MSG = "ERROR: An unhandled exception was encountered."
TEST_CONTEXT = {
    "OS": "osx 10.14.6",
    "py_version": "3.8.0",
    "app": "cci",
    "sf_api_version": "47.0",
}


@pytest.mark.django_db
class TestUser:
    pass


@pytest.mark.django_db
@freeze_time("1970-01-01")
class TestModels:
    """Single test class for all models to minimize DB setup/teardown time."""

    def test_error_instance_model(self):
        stacktrace = "stacktrace"

        error_instance = ErrorInstance.objects.create(
            message=TEST_ERROR_MSG, context=TEST_CONTEXT, stacktrace=stacktrace
        )

        assert error_instance.context == TEST_CONTEXT
        assert error_instance.message == TEST_ERROR_MSG
        assert error_instance.stacktrace == stacktrace
        assert error_instance.created == datetime(1970, 1, 1, tzinfo=timezone.utc)

    def test_situation_model(self):
        situation = Situation.objects.create(
            error_msg=TEST_ERROR_MSG, context=TEST_CONTEXT
        )

        assert situation.error_msg == TEST_ERROR_MSG
        assert situation.context == TEST_CONTEXT
        assert situation.created == datetime(1970, 1, 1, tzinfo=timezone.utc)

    def test_solution_model(self):
        solution_type = 1
        solution_text = "Please retry the last command."

        solution = Solution.objects.create(
            solution_type=solution_type, text=solution_text, situation=None
        )

        assert solution.solution_type == solution_type
        assert solution.text == solution_text
        assert solution.situation == None
        assert solution.created == datetime(1970, 1, 1, tzinfo=timezone.utc)
