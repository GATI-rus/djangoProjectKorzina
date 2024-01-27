from django import forms
from .models import *
from django.core.validators import RegexValidator

class OrderForm(forms.Form):
    adres = forms.CharField(label='Адрес доставки')
    tel = forms.CharField(label='Телефон', validators=[RegexValidator('^\+7-\d{3}-\d{3}-\d{2}-\d{2}$', 'Введите номер телефона в формате +7-XXX-XXX-XX-XX')], required=True)
    email = forms.EmailField(label='Эл.почта')