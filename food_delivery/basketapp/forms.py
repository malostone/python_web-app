from django import forms
from django.forms import ModelForm
from basketapp.models import Order, OrderItems


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['address', 'phone']

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
