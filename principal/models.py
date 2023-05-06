from django.contrib.auth.models import User
from django.db import models


class Annotation(models.Model):
    account = models.ForeignKey(User, null=False, blank=False, on_delete=models.SET_NULL)
    name = models.CharField(max_length=45)
    description = models.TextField()
    deadline = models.DateTimeField()  # format("YYYY-MM-DD\ HH:mn:sc")
    reminder = models.TimeField()  # format("HH:Mn:Sc")
    over = models.BooleanField(default=False)
    objects = models.Manager()
