from django.test import TestCase
from core.models import Beer


class ModelTestCase(TestCase):
    """This class defines the test suite for the beer model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.beer_name = "Beer"
        self.beer = Beer(name=self.beer_name)

    def test_model_can_create_a_beer(self):
        """Test the beer model can create a beer."""
        old_count = Beer.objects.count()
        self.beer.save()
        new_count = Beer.objects.count()
        self.assertNotEqual(old_count, new_count)
