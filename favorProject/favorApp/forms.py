from .models import Favor

from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime


class AddFavorForm(ModelForm):
    class Meta:
        model = Favor
        exclude = []
        # fields = ["date"]
        help_texts = {
            'date': _('Date of event, enter a date between now and 4 weeks.'),
        }
        # widgets = {'myDateField': forms.DateInput(
        #     attrs={'id': 'datetimepicker12'})
        # }
        # error_messages = {
        #     'name': {
        #         'max_length': _("This writer's name is too long."),
        #     },
        # }

    def clean_date(self):
        print("cleaning date")
        data = self.cleaned_data['date']

        # Check if a date is not in the past.
        if data < datetime.date.today():
            raise ValidationError(
                _('Invalid date - start date of event in past'))

        # Check if a date is in the allowed range (+4 weeks from today).
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(
                _('Invalid date - start date more than 4 weeks ahead'))

        # Remember to always return the cleaned data.
        return data


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(
        max_length=30, required=True, help_text='Required.')
    email = forms.EmailField(
        max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2', )
