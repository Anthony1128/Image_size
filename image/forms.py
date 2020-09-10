from django import forms
import requests
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
        image_content_type = requests.get(url).headers['Content-Type']

        # запрет на не заполнение обеих форм
        if not file and not url:
            raise forms.ValidationError('One of fields is required')

        # запрет на заполнение обеих форм
        elif file and url:
            raise forms.ValidationError('Only one of fields is required')

        # проверка url на формат
        elif image_content_type != 'image/jpeg':
            raise forms.ValidationError('Wrong URL')
        return self.cleaned_data


# Форма для изменения размеров изображения
class ChangeForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['width', 'height']

    # сохранение пропорций
    def clean(self):
        width = self.cleaned_data.get('width')
        height = self.cleaned_data.get('height')

        # запрет на не заполнение обеих форм
        if not width and not height:
            raise forms.ValidationError('At least one of fields is required')
        return self.cleaned_data

