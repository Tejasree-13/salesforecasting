from django import forms
from .models import Sale

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['gender', 'age', 'category', 'price', 'quantity', 'payment_method']
        
