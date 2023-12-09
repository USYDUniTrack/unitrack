from django.db import models

class Units(models.Model):
    unit_code = models.CharField(null = False, max_length = 8)
    unit_name = models.CharField(null = True, max_length = 100)

    def __str__(self):
        return self.unit_code
