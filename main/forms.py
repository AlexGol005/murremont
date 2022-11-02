from django import forms


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







