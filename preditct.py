import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Sample data (you should replace this with your actual data)
data = pd.read_csv("dscovr_data_2018.txt", delim_whitespace=True)

data['is_mr'] = np.where(data['field'] <= -10, True, False)

print(data.head())
# Split the data into features (X) and labels (y)
X = data[['field']]
y = data['is_mr']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train a logistic regression model (you can use other models as well)
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions on new data
new_value = [[90]]  # Replace this with the value you want to predict
prediction = model.predict(new_value)

if prediction[0] == 1:
    print("The next value is predicted to be interesting.")
else:
    print("The next value is predicted to be not interesting.")
