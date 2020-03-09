from django.test import TestCase
from django.utils import timezone

from favorApp.forms import AddFavorForm


class AddFavorFormTest(TestCase):
    def test_field_label(self):
        form = AddFavorForm()
        self.assertTrue(form.fields['title'].label == 'Title')
        self.assertTrue(
            form.fields['number_of_favors'].label == 'Number of favors')

    def test_field_help_text(self):
        form = AddFavorForm()
        self.assertEqual(form.fields['date'].help_text,
                         'Enter a date between now and 4 weeks.')

    def test_date_in_past(self):
        date = timezone.now() - timezone.timedelta(days=1)
        form = AddFavorForm(data={'date': date})
        self.assertFalse(form.is_valid())

    def test_date_too_far_in_future(self):
        date = timezone.now() + timezone.timedelta(weeks=4) + \
            timezone.timedelta(days=1)
        form = AddFavorForm(data={'date': date})
        self.assertFalse(form.is_valid())

    def test_date_today(self):
        date = timezone.now()
        form = AddFavorForm(data={'date': date})
        self.assertFalse(form.is_valid())
