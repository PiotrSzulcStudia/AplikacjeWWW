
from django.db import models

class District(models.Model):
    name = models.CharField(max_length=200)
    parentId = models.ForeignKey("self", null=True)

    def __str__(self):
        return self.name.encode('utf8')

class Commission(models.Model):
    name = models.CharField(max_length=200)
    parentId = models.ForeignKey(District)
    receivedCardsToVote = models.IntegerField(default=0)
    votersAllowedToVote = models.IntegerField(default=0)

    def __str__(self):
        return self.name.encode('utf8')
