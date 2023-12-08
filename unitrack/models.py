from django.db import models

class MyModel(models.Model):
    image = models.ImageField(upload_to='images/')
