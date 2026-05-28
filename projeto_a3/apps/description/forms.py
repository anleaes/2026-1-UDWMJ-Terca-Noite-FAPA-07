from django import forms
from .models import Description

class DescriptionForm(forms.ModelForm):

    class Meta:
        model = Description
        exclude = ()
