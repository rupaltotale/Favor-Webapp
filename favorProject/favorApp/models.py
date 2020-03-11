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
    confirmedUsers = models.ManyToManyField(User, related_name='confirmed_users')

    def __str__(self):
        return "Title: {}, Description: {}, Owner: {}".format(self.title, self.description, self.owner)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    number_of_favors = models.IntegerField(blank=False, default=5)

    def __str__(self):
        return "User: {}, favors: {}".format(self.user, self.number_of_favors)