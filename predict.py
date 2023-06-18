from tensorflow.keras.models import load_model  
import joblib  # Importing joblib for loading scaler objects
import pandas as pd
import numpy as np

past_years = 7  # Number of past years

# Loading a dictionary to hold the data for each month
data_per_month = {}
for month in range(1, 13):
    data_per_month[month] = pd.read_csv(f'data_per_month_values/data_month_{month}.csv') 

def load_model_and_scaler(month):
    model = load_model(f'models\model4\model_{month}.h5')  # Loading the models
    scaler = joblib.load(f'models\model4\scaler_{month}.pkl')  # Loading the scalers
    
    return model, scaler  # Returning the model and the scaler

def predict_accidents(year, month):
    # Preparing the data for prediction, based on past years' data for the specified month
    data_to_predict = data_per_month[month][data_per_month[month]['year'] < year]['value'].values[-past_years:]
    data_to_predict = data_to_predict.reshape((1, 1, past_years))

    # Loading the model and the scaler for the specified month
    model, scaler = load_model_and_scaler(month)

    # Making the prediction
    prediction = model.predict(data_to_predict)
    # Inversing the transformation to get the actual value
    prediction = scaler.inverse_transform(prediction)
    
    return prediction.item()  # Returning the prediction as a single value
