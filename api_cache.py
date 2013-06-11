
from django.db import models




class SkillGroup(models.Model):
    groupID = models.IntegerField(primary_key=True)
    typeName = models.CharField(max_length=100)


class Skill(models.Model):
    typeID = models.IntegerField(primary_key=True)
    groupID = models.ForeignKey(SkillGroup)
    typeName = models.CharField(max_length=100)
    description = models.TextField()
    published = models.BooleanField()
    rank = models.PositiveSmallIntegerField()
    primaryAttribute = models.CharField(max_length=25)
    secondaryAttribute = models.CharField(max_length=25)
    canNotBeTrainedOnTrial = models.PositiveSmallIntegerField()


class SkillRequirement(models.Model):
    skill = models.ForeignKey(Skill)
    required_skill = models.ForeignKey(Skill)
    level = models.PositiveSmallIntegerField()

