import factory
from django.contrib.auth.models import User
from favorApp.models import Favor
from django.utils import timezone

class UserFactory(factory.Factory):
    class Meta:
        model = User

    first_name = 'John'
    last_name = 'Doe'
    email = factory.Sequence(lambda n: 'johndoe{0}@johndoe.com'.format(n))
    username = factory.Sequence(lambda n: 'johndoe{0}@johndoe.com'.format(n))
    password = factory.PostGenerationMethodCall('set_password', 'password')


class AdminFactory(factory.DjangoModelFactory):
    class Meta:
        model = User
    
    email = 'admin@admin.com'
    username = 'admin'
    password = 'adm1n'

    is_superuser = True
    is_staff = True
    is_active = True
    

class FavorFactory(factory.Factory):
    class Meta:
        model = Favor

    title = 'Massage'
    description = 'Massage'
    number_of_favors = 3
    date = timezone.now() + timezone.timedelta(weeks=2)
    location = 'location'
