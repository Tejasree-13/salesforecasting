from django.shortcuts import render
from .forms import SaleForm  # Import your SaleForm from forms.py
from .models import Sale  # Import your Sale model from models.py
from django.http import HttpResponse
import joblib
import random

model = joblib.load('model.pkl')
def sale(request):
    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            form.save()
            gender = form.cleaned_data['gender']
            age = form.cleaned_data['age']
            category = form.cleaned_data['category']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']
            payment_method = form.cleaned_data['payment_method']
            random_int = (random.randint(1,10))
            shopping_mall = (random_int)
            # shopping_mall = form.cleaned_data['shopping_mall']
            input_data= [[gender,age,category,price,quantity,payment_method,shopping_mall]]
            prediction = model.predict(input_data)
            return render(request, 'sales_form.html', {'response' : prediction})
    else:
        form = SaleForm()
    return render(request, 'sales_form.html', {'form': form})
