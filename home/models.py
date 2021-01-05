from django.db import models

# Create your models here.
class contactdata (models.Model):
    # id: int - primary key..it is automatically available in database..
    # we are assigning the value so it will replace : to = sign , if we miss = sign so we can't create table in database.
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    comment = models.TextField()