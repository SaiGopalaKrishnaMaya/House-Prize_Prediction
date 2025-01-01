import os
import joblib
import pandas as pd
from django.shortcuts import render
from .forms import HousePriceForm
from django.http import HttpResponse
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def train_model():
    # Load the dataset
    data = pd.read_csv(r'final_dataset.csv')
    print(data)

    # Drop unnecessary columns
    df = data.drop(columns=['Unnamed: 0', 'zip_code'])
    x = df[['beds', 'baths', 'size']]
    y = df['price']

    # Train-test split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    # Train the model
    model = LinearRegression()
    model.fit(x_train, y_train)

    # Return the trained model (no saving to file)
    return model

def index(request):
    predicted_price = None

    # Train the model in memory (if not already trained)
    model = train_model()

    if request.method == 'POST':
        form = HousePriceForm(request.POST)
        if form.is_valid():
            beds = form.cleaned_data['beds']
            baths = form.cleaned_data['baths']
            size = form.cleaned_data['size']
            
            try:
                # Prepare the input data
                new_data = {'beds': beds, 'baths': baths, 'size': size}
                new_data_df = pd.DataFrame(new_data, index=[0])
                
                # Make the prediction using the trained model
                predicted_price = model.predict(new_data_df)[0]
            except Exception as e:
                return HttpResponse(f"Error: {e}", status=500)
    else:
        form = HousePriceForm()
    
    return render(request, 'hello/index.html', {'form': form, 'predicted_price': predicted_price})
