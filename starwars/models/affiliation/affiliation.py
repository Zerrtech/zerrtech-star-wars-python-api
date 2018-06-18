from django.db import models

class Affiliation(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name