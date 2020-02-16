from django.test import TestCase
from favorApp.models import Favor
from django.utils import timezone


# Create your tests here.
# Test template based off of https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing


class FavorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("Running FavorModelTest...")
        # Set up non-modified objects used by all test methods
        Favor.objects.create(title='Back Massage',
                             description='The best back massage in SLO.',
                             number_of_favors=2,
                             date=timezone.now(),
                             location="San Luis Obispo, CA",
                             )

    def test_title_label(self):
        favor = Favor.objects.get(id=1)
        field_label = favor._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    def test_description_label(self):
        favor = Favor.objects.get(id=1)
        field_label = favor._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'description')

    def test_first_name_max_length(self):
        favor = Favor.objects.get(id=1)
        max_length = favor._meta.get_field('title').max_length
        self.assertEquals(max_length, 256)

    def test_object_name_formatting(self):
        favor = Favor.objects.get(id=1)
        expected_object_name = "Title: {}, Description: {}, Owner: {}".format(
            favor.title, favor.description, favor.owner)
        self.assertEquals(expected_object_name, str(favor))
