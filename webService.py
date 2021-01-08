import numpy as np
import flask as fl
import tensorflow.keras as kr
from flask import jsonify

app = fl.Flask(__name__)

# Set default route
@app.route("/")
def home():
    return app.send_static_file('index.html')

#recieve the user input with var input
#call in the model and use model.predict with the user input to generate a result
# output the result
@app.route("/api/predict/<speed>")
def power(input):
    model = kr.models.load_model('datamodel.h5')
    input = float(input)
    result = model.predict([input])
    print(result)
    return jsonify({"value":result.item(0)})
