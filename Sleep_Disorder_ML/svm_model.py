# In this file, the SVM model is implemented and it is used to predict whether a person has a sleep disorder or not

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Loading the dataset
df = pd.read_csv('Sleep_health_and_lifestyle_dataset.csv')

# Preprocessing of data - encoding categorical values
df = pd.get_dummies(df, columns=['Gender', 'Occupation', 'Sleep Disorder'])

# Spliting data - features and target variable - target variable in this case is Insomnia
x = df.drop(['Person ID', 'BMI Category', 'Blood Pressure'], axis=1)
y = df['Sleep Disorder_Insomnia']


# Train test split of data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# SVM
svm_classifier = SVC(kernel='linear')
svm_classifier.fit(x_train, y_train)

# Feature importance of model
f_importance = np.abs(svm_classifier.coef_[0])
f_importancedf = pd.DataFrame({'Feature': x.columns, 'Importance': f_importance})
f_importancedf = f_importancedf.sort_values(by='Importance', ascending=False)

top_n_important_features = 10
print(f'Top {top_n_important_features} features: ')
print(f_importancedf.head(top_n_important_features))

# Predictions from the model
y_predict = svm_classifier.predict(x_test)

# Evaluation of the model
accuracy = accuracy_score(y_test, y_predict)
report = classification_report(y_test, y_predict)

print(f'The accuracy of the SVC model is: {accuracy}')
print(report)

# Save the SVC model using joblib 
joblib.dump(svm_classifier, 'svm_model.pkl')

# Load the model to predict
model_for_prediction = joblib.load('svm_model.pkl')

# Select a row for prediction (replace 1 with the index of the row you want to predict)
prediction_row = x_test.iloc[0:12]  # This selects the second row from the test data
predictions = model_for_prediction.predict(prediction_row)

print(f'Predictions of insomnia for the selected rows in the dataset: {predictions}')


# Spliting data - features and target variable - target variable in this case is Insomnia
x = df.drop(['Person ID', 'BMI Category', 'Blood Pressure'], axis=1)
y = df['Sleep Disorder_Sleep Apnea']


# Train test split of data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# SVM
svm_classifier = SVC(kernel='linear')
svm_classifier.fit(x_train, y_train)

# Predictions from the model
y_predict = svm_classifier.predict(x_test)

# Save the SVC model using joblib 
joblib.dump(svm_classifier, 'svm_model_apnea.pkl')

# Load the model to predict
apnea_model_for_prediction = joblib.load('svm_model_apnea.pkl')

# Select a row for prediction (replace 1 with the index of the row you want to predict)
prediction_rows = x_test.iloc[0:12]  # This selects the second row from the test data
apnea_predictions = apnea_model_for_prediction.predict(prediction_rows)

print(f'Predictions of sleep apnea for the selected rows in the dataset: {apnea_predictions}')

