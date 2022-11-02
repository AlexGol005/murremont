from django import forms
from django.db.models import  Q

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from .models import *


class OrderForm(forms.ModelForm):
    """форма для заказа"""

    name = forms.CharField(label='Ваше имя', max_length=100, required=True,
                           widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': 'Имя'}
                                                  ))
    telephone = forms.CharField(label='Телефон для связи', max_length=12, required=True,
                           widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': '89500484071'}
                                                  ))
    adress = forms.CharField(label='Адрес работ', max_length=1000, required=False,
                                widget=forms.TextInput(attrs={'class': 'form-control',
                                                              'placeholder': 'адрес'}
                                                       ))
    comment = forms.CharField(label='Описание, комментарии (не обязательно)', max_length=10000, required=False,
                             widget=forms.Textarea(attrs={'class': 'form-control'}))


    class Meta:
        model = Order
        fields = ['person',
                  'telephone',
                  'adress',
                  'comment',
                  ]



class SearchForm(forms.Form):
    "форма для поиска по списку работ"
    name = forms.CharField(label='Найти')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-10 mb-0'),
                Submit('submit', 'Найти', css_class='btn  btn-info col-md-2 mb-3 mt-4 ml-4'),
                css_class='form-row'
            ))




