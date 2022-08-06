from django import forms
import requests
from .models import Image


# New image adding form
class AddForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['url', 'file']

    # redefinition of method clean
    def clean(self):
        file = self.cleaned_data.get('file')
        url = self.cleaned_data.get('url')

        # constraint on both form not filled
        if not file and not url:
            raise forms.ValidationError('One of fields is required')

        # constraint on both form filled
        elif file and url:
            raise forms.ValidationError('Only one of fields is required')

        # check url format
        elif url and requests.get(url).headers['Content-Type'] != 'image/jpeg':
            raise forms.ValidationError('Wrong URL')
        return self.cleaned_data


# Form for changing image size
class ChangeForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['width', 'height']

    #  save proportions
    def clean(self):
        width = self.cleaned_data.get('width')
        height = self.cleaned_data.get('height')

        # constraint on both form not filled
        if not width and not height:
            raise forms.ValidationError('At least one of fields is required')
        return self.cleaned_data

