"""
Flask API of the SMS Spam detection model model.
"""
import joblib
from flask import Flask, jsonify, request
from flasgger import Swagger
from waitress import serve
import pandas as pd
import os
import urllib.request
import zipfile

from text_preprocessing import prepare, _extract_message_len, _text_process

model_url = os.environ.get('MODEL_URL')

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/predict', methods=['POST'])
def predict():
    """
    Predict whether an SMS is Spam.
    ---
    consumes:
      - application/json
    parameters:
        - name: input_data
          in: body
          description: message to be classified.
          required: True
          schema:
            type: object
            required: sms
            properties:
                sms:
                    type: string
                    example: This is an example of an SMS.
    responses:
      200:
        description: "The result of the classification: 'spam' or 'ham'."
    """
    input_data = request.get_json()
    sms = input_data.get('sms')
    processed_sms = prepare(sms)
    prediction = app.model.predict(processed_sms)[0]
    
    res = {
        "result": prediction,
        "classifier": "decision tree",
        "sms": sms
    }
    print(res)
    return jsonify(res)

if __name__ == '__main__':
    if not os.path.isfile("output/model.joblib") or not os.path.isfile("output/preprocessor.joblib"):
        print("models not found, attempting download")
        urllib.request.urlretrieve(model_url, "output.zip")
        with zipfile.ZipFile("output.zip") as output_zip:
           output_zip.extractall(".") # the output zip contains a folder named output
        print("models downloaded and extracted into output folder")

    app.model = joblib.load('output/model.joblib') 
    
    port = int(os.environ.get('MODEL_PORT', 8081))

    # Use waitress instead of the debug WSGI server
    # As suggested in https://stackoverflow.com/a/54381386
    print("serving model using waitress serve")
    serve(app, host="0.0.0.0", port=port)
