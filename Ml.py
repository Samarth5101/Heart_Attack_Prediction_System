import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

def make_prediction(new_data):
    # Load the dataset
    df = pd.read_csv("Medicaldataset.csv")

    # Split the dataset into features (X) and target (y)
    X = df.drop('Result', axis=1)
    y = df['Result']

    # Split the dataset into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)


    model = LogisticRegression()
    model.fit(X_train_scaled, y_train)


    new_df = pd.DataFrame(new_data)
    new_df_scaled = scaler.transform(new_df)




    # Making prediction
    prediction = model.predict(new_df_scaled)

    return prediction

# Example:
new_data = {
    'Age': [40],
    'Gender': [0],
    'Heart rate': [70],
    'Systolic blood pressure': [120],
    'Diastolic blood pressure': [80],
    'Blood sugar': [150],
    'CK-MB': [2.0],
    'Troponin': [0.02],
}

result1 = make_prediction(new_data)
print("Prediction:", result1)

new_data2 = {
    'Age': [69],
    'Gender': [1],
    'Heart rate': [50],
    'Systolic blood pressure': [130],
    'Diastolic blood pressure': [90],
    'Blood sugar': [110],
    'CK-MB': [1.5],
    'Troponin': [0.08],
}
result2 = make_prediction(new_data2)
print("Prediction:", result2)

new_data3 = {
    'Age': [63],
    'Gender': [1],
    'Heart rate': [66],
    'Systolic blood pressure': [160],
    'Diastolic blood pressure': [83],
    'Blood sugar': [160],
    'CK-MB': [1.8],
    'Troponin': [0.012],
}
result3 = make_prediction(new_data3)
print("Prediction:", result3)

