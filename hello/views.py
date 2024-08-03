import os
import joblib
import pandas as pd
from django.shortcuts import render
from .forms import HousePriceForm
from django.http import HttpResponse

def index(request):
    predicted_price = None
    model_path = model_path = r'house_price_model.pkl'

    if request.method == 'POST':
        form = HousePriceForm(request.POST)
        if form.is_valid():
            beds = form.cleaned_data['beds']
            baths = form.cleaned_data['baths']
            size = form.cleaned_data['size']
            
            try:
                model = joblib.load(model_path)
                new_data = {'beds': beds, 'baths': baths, 'size': size}
                new_data_df = pd.DataFrame(new_data, index=[0])
                predicted_price = model.predict(new_data_df)[0]
            except FileNotFoundError:
                return HttpResponse("Model file not found.", status=500)
    else:
        form = HousePriceForm()
    
    return render(request, 'hello/index.html', {'form': form, 'predicted_price': predicted_price})
