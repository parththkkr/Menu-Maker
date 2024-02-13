from django import forms
from .models import OrderedItem

class OrderForm(forms.Form):
    def __init__(self, *args, **kwargs):
        items = kwargs.pop('items')
        super(OrderForm, self).__init__(*args, **kwargs)

        for item in items:
            self.fields[f'item_{item.id}'] = forms.IntegerField(label=item.itemObj.name, min_value=1, initial=0)

    def clean(self):
        cleaned_data = super().clean()
        total_quantity = sum(cleaned_data.get(key, 0) for key in cleaned_data.keys() if key.startswith('item_'))

        if total_quantity == 0:
            raise forms.ValidationError("Please select at least one item.")
