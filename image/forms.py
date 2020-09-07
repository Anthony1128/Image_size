from django import forms
from .models import Image


class AddForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['url', 'file']

    def clean(self):
        file = self.cleaned_data.get('file')
        url = self.cleaned_data.get('url')
        if not file and not url:
            raise forms.ValidationError('One of fields is required')
        elif file and url:
            raise forms.ValidationError('Only one of fields is required')
        return self.cleaned_data

    # def __init__(self, *args, **kwargs):
    #     super(AddForm, self).__init__(*args, **kwargs)
    #     self.fields['file'].required = False


class ChangeForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['width', 'height']