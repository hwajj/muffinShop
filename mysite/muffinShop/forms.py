from datetime import datetime

from django import forms

from . import models
from .models import Product, OrderItem, Order
from django.core.validators import RegexValidator
#
# class InputForm(forms.ModelForm):
#
#     class Meta:
#         model = OrderItem
#         fields = ('quantity',)


class InputForm(forms.Form):
    product_number = forms.IntegerField(min_value=1,max_value=11, initial=1, label="품번")
    quantity = forms.IntegerField(min_value=1,max_value=10, initial=1, required=False, label="수량", help_text='개')


class NumberForm(forms.Form):
    number = forms.CharField(max_length=11,label='휴대폰번호')


class OrderForm(forms.ModelForm):
    order_date = forms.DateField(initial=datetime.now(), label="주문일")
    user_name = forms.CharField(max_length=20, label="성함")
    user_phone = forms.CharField(max_length=20, label="폰번호")
    user_address = forms.CharField(max_length=50, label="주소")
    class Meta:
        model = Order
        fields = [
            'order_date', 'user_name', 'user_phone', 'user_address'
        ]

#
# def phone_validator:
#     phone_number_validator= RegexValidator(r'^01([0|1|6|7|8|9]?)-?([0-9]{3,4})-?([0-9]{4})$')