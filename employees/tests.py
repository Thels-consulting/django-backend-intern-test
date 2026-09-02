from django.test import TestCase


class SetupSanityTests(TestCase):
    """
    Confirms the project boots and `python manage.py test` runs cleanly
    before you've written any code. Feel free to delete this once you
    have real tests below.
    """

    def test_environment_is_configured(self):
        self.assertTrue(True)


# TODO (candidate): Add your own tests below. At minimum, cover:
#   - Department creation
#   - Employee creation
#   - Employee listing
#   - Employee retrieval
#   - Duplicate email validation (should be rejected)
#   - Negative salary validation (should be rejected)
#   - Department filtering (e.g. ?department=<id>)
#   - Authentication restrictions (writes require login, reads don't)
#
# Tip: rest_framework.test.APITestCase is generally a better fit than
# django.test.TestCase for exercising the API endpoints themselves.
