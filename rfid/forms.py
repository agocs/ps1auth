from django.forms import ModelForm
from .models import RFIDNumber


class KeyForm(ModelForm):
    class Meta:
        model = RFIDNumber
        exclude = ['user']

