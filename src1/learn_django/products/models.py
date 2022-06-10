# when we make changes to our model
# we have to write python manage.py makemigrations
# followed by python manage.py migrate

from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)  # CharField requires the max_length argument
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    # blank has to deal with how the fill is rendered (like required field)
    # null has to deal with the database
    # so when we coded blank=True, then summary was not bold.
    # but when we change it to False, the summary again become bold.
    # blank deals with the field, null deal with the database.
    summary = models.TextField(blank=False, null=False)
    featured = models.BooleanField(default=False)
