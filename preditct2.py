import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score

# Load your historical time series data into a Pandas DataFrame
data = pd.read_csv('dscovr_data_2018.txt', delim_whitespace=True)

# Create a binary label for each data point based on the presence of the value of interest in the next 60 values
data['is_mr'] = data['field'].rolling(60).apply(lambda x: any(x<=-10), raw=True).astype(int).shift(-59)

# Extract relevant features from your data (if needed)

# Create a sliding window of size 60
window_size = 60
X = []
y = []

for i in range(len(data) - window_size):
    window = data['field'].iloc[i:i + window_size].values
    target = data['is_mr'].iloc[i + window_size]
    X.append(window)
    y.append(target)

X = np.array(X)
y = np.array(y)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a binary classification model (e.g., Logistic Regression)
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred_proba = model.predict_proba(X_test)[:, 1]  # Probability of the positive class

# Calculate the ROC AUC score (or other appropriate metrics)
roc_auc = roc_auc_score(y_test, y_pred_proba)
print("ROC AUC Score:", roc_auc)

# Use the trained model for predictions on your historical data to get probability scores
historical_data_probabilities = model.predict_proba(X)[:, 1]
