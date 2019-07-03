from django.db import models


class Beer(models.Model):
    """Beers rated in the app."""

    name = models.CharField(max_length=255, blank=False, unique=True)
    ibu = models.IntegerField(default=55)
    calories = models.FloatField(max_length=5, default=0)
    abv = models.FloatField(max_length=3, default=0)
    style = models.CharField(max_length=50, default="Bitter")
    brewery_location = models.CharField(max_length=50, default="Some Brewery")
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "f{(self.name)}"
