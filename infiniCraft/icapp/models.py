from django.db import models

class Btn(models.Model):
    label = models.CharField(max_length=128)
    emoji = models.CharField(max_length=16)

    def __str__(self):
        return self.label