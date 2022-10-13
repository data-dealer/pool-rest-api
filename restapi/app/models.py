from django.db import models
from django.contrib.postgres.fields import ArrayField

class Pool(models.Model):
    poolId = models.IntegerField(primary_key=True)
    poolValues = ArrayField(models.FloatField(), default=list, null=True, blank=True)

    def __str__(self):
        return self.poolId
