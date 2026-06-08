from django import forms
from .models import Support

class SupportForm(forms.ModelForm):

    class Meta:
        model = Support
        exclude = ()
