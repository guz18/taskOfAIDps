from flask import Flask, request, jsonify 
import os
from predict import predict_accidents  # Importing the function from the predict.py file 

app = Flask(__name__)  # Initializing the Flask application

@app.route('/', methods=['GET', 'POST'])  # Defining the route for the endpoint
def home():
    if request.method == 'POST':  # Handling POST requests
        data = request.get_json(force=True)  # Extracting data from the request
        year = int(data['year'])  
        month = int(data['month'])  

        # Checking the year value for constraints
        if year < 2007:
            return jsonify({
                'error': 'Unfortunately, because I have information from the year 2000 and trained to make predictions with the previous seven years, I can not make prediction to this date.'
            }), 400
        elif year > 2021:
            return jsonify({
                'error': 'I don\'t have data to make prediction after the year 2021 unfortunately.'
            }), 400

        # Making a prediction using the imported function
        prediction = predict_accidents(year, month)

        if prediction is None:  # Handling the case when prediction is not successful
            return jsonify({
                'error': 'Could not make a prediction.'
            }), 400
        else:  # Returning the prediction in JSON format
            return jsonify({
                'prediction': prediction
            }), 200
    else:  # Handling GET requests
        return 'Welcome!'

# Running the Flask application
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)