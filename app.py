from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome!'

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    year = int(data['year'])
    month = int(data['month'])
    prediction = predict_accidents(year, month)

    if prediction is None:
        return jsonify({
            'error': 'Could not make a prediction.'
        }), 400
    else:
        return jsonify({
            'prediction': prediction[0][0]
        }), 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(port=port, debug=True)
