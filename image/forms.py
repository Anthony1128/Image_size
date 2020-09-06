from django import forms
from .models import Image


class AddForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['file']
