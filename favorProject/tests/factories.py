import factory
from django.contrib.auth.models import User
from favorApp.models import Favor
from django.utils import timezone

class UserFactory(factory.Factory):
    class Meta:
        model = User

    first_name = 'John'
    last_name = 'Doe'
    username = "johndoe"
    password = factory.PostGenerationMethodCall('set_password', 'password')


class FavorFactory(factory.Factory):
    class Meta:
        model = Favor

    title = 'Massage'
    description = 'Massage'
    number_of_favors = 3
    date = timezone.now() + timezone.timedelta(weeks=2)
    location = 'location'
    volunteer_event = False
    requester_signed = False
    giver_signed = False