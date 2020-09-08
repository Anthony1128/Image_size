from django import forms
from .models import Image


# форма добавления нового изображения
class AddForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['url', 'file']

    # переопределение метода clean
    def clean(self):
        file = self.cleaned_data.get('file')
        url = self.cleaned_data.get('url')

        # запрет на не заполнение обеих форм
        if not file and not url:
            raise forms.ValidationError('One of fields is required')

        # запрет на заполнение обеих форм
        elif file and url:
            raise forms.ValidationError('Only one of fields is required')
        return self.cleaned_data


# Форма для изменения размеров изображения
class ChangeForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['width', 'height']