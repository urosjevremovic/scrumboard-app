from django.db import models


class List(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Card(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    list = models.ForeignKey(List, related_name='cards', on_delete=models.CASCADE)
    story_points = models.PositiveIntegerField(null=True, blank=True)
    business_value = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.title
