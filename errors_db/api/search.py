from errors_db.api.models import Solution


class ErrorSearch:
    """Class to manage search behaviors."""

    @classmethod
    def get_solutions(cls, error_msg, stacktrace, context):
        """Exact string match on error message for now."""
        return Solution.objects.filter(situation__error_msg=error_msg)

