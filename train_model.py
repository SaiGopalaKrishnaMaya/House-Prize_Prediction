import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import joblib


data = pd.read_csv(r'final_dataset.csv')
print(data)


print(data.columns)
df=data.drop(columns=['Unnamed: 0','zip_code'])
print(df)

x = df[['beds', 'baths', 'size']]
y = df['price']

plt.scatter(x['size'], y)  # You can replace 'size' with other features
plt.xlabel('Size')
plt.ylabel('Price')
plt.title('Price vs Size')
plt.show()

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(x_train, y_train)

joblib.dump(model, 'house_price_model.pkl')

new_data = {'beds': 3, 'baths': 2.5, 'size': 1500}
new_data_df = pd.DataFrame(new_data, columns=x.columns, index=[0])
predicted_price = model.predict(new_data_df)
print("Predicted price:", predicted_price)

