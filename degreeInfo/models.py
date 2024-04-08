from django.db import models

class Units(models.Model):
    unit_code = models.CharField(null = False, max_length = 8)
    unit_name = models.CharField(null = True, max_length = 100)

    def __str__(self):
        return self.unit_code

class Degree(models.Model):
    degrees = models.CharField(
        max_length = 256,
    )
    majors = models.CharField(
        max_length = 256,
    )
    second_majors = models.CharField(
        max_length = 256,
    )
    minors = models.CharField(
        max_length = 256,
    )
