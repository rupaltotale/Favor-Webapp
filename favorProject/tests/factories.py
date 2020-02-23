import factory
from django.contrib.auth.models import User

class UserFactory(factory.Factory):
    class Meta:
        model = User

    first_name = 'John'
    last_name = 'Doe'
    username = "johndoe"
    password = factory.PostGenerationMethodCall('set_password', 'password')