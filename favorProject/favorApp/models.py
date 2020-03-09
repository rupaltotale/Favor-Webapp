from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Favor(models.Model):
    title = models.CharField(max_length=256, blank=False)
    description = models.CharField(max_length=256, blank=False)
    number_of_favors = models.IntegerField(blank=False)
    date = models.DateTimeField(
        auto_now=False, auto_now_add=False, blank=False)
    location = models.CharField(max_length=256, blank=False)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    pendingUsers = models.ManyToManyField(User, related_name='pending_users')
    # volunteer_event = models.BooleanField(default=False)
    # requester_signed = models.BooleanField(default=False)
    # giver_signed = models.BooleanField(default=False)

    def __str__(self):
        return "Title: {}, Description: {}, Owner: {}".format(self.title, self.description, self.owner)
