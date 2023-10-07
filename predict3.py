import pandas as pd
import numpy as np
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error

# Load your historical time series data into a Pandas DataFrame
data = pd.read_csv('dscovr_data_2018.txt', delim_whitespace=True)
target_value = 42  # Replace with your specific target value

# Preprocess the data as needed

# Train-test split (for model evaluation)
train_data = data.iloc[:-60]  # Use all except the last 60 data points for training
test_data = data.iloc[-60:]  # Use the last 60 data points for testing

# Fit an ARIMA model
model = ARIMA(train_data['value_column'], order=(5,1,0))  # Adjust the order as needed
model_fit = model.fit(disp=0)

# Make predictions for the test set
predictions = model_fit.forecast(steps=len(test_data))

# Calculate RMSE (Root Mean Squared Error) to evaluate the model's performance
rmse = np.sqrt(mean_squared_error(test_data['value_column'], predictions))
print(f"RMSE: {rmse}")

# Check if the specific target value appears in the predictions
target_appears = np.isin(target_value, predictions)

if target_appears:
    print(f"The target value {target_value} is predicted to appear in the next 60 values.")
else:
    print(f"The target value {target_value} is not predicted to appear in the next 60 values.")
