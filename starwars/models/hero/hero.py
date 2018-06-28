from django.db import models
from starwars.models.affiliation.affiliation import Affiliation

class Hero(models.Model):
    class Meta:
        verbose_name_plural = "Heroes"

    name = models.CharField(max_length=128)
    power = models.IntegerField()
    # add affiliations model
    light = models.BooleanField()
    imageUrl = models.CharField(max_length=128)
    affiliations = models.ManyToManyField(Affiliation)


    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

