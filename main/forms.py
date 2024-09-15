from django import forms
from django.forms import BooleanField

from main.models import Product, Version


blocked_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class StyleMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleMixin, forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('seller',)

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']

        for word in blocked_words:
            if word.lower() in cleaned_data.lower():
                raise forms.ValidationError("В названии содержатся запрещенные слова")

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']

        for word in blocked_words:
            if word.lower() in cleaned_data.lower():
                raise forms.ValidationError("В описании содержатся запрещенные слова")

        return cleaned_data


class VersionForm(StyleMixin, forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'

    def clean_version_index(self):
        cleaned_data = self.cleaned_data['version_index']

        for word in blocked_words:
            if word.lower() in cleaned_data.lower():
                raise forms.ValidationError("В названии содержатся запрещенные слова")

        return cleaned_data

    def clean_version_name(self):
        cleaned_data = self.cleaned_data['version_name']

        for word in blocked_words:
            if word.lower() in cleaned_data.lower():
                raise forms.ValidationError("В названии содержатся запрещенные слова")

        return cleaned_data