from .models import Favor

from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from bootstrap_datepicker_plus import DateTimePickerInput


class AddFavorForm(ModelForm):
    class Meta:
        model = Favor
        exclude = ["pendingUsers", "confirmedUsers", "owner"]
        # fields = ["date"]
        help_texts = {
            'date': _('Enter a date between now and 4 weeks.'),
        }
        widgets = {'date': DateTimePickerInput()}

    def clean_date(self):
        data = self.cleaned_data['date']

        # Check if a date is not in the past.
        if data < timezone.now():
            raise ValidationError(
                _('Invalid date - start date of event in past'))

        # Check if a date is in the allowed range (+4 weeks from today).
        if data > timezone.now() + timezone.timedelta(weeks=4):
            raise ValidationError(
                _('Invalid date - start date more than 4 weeks ahead'))

        # Remember to always return the cleaned data.
        print("Printing data:", self.cleaned_data)
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
