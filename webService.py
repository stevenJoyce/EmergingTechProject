import numpy as np
import flask as fl
import tensorflow.keras as kr
from flask import jsonify

app = fl.Flask(__name__)

# Set default route
@app.route("/")
def home():
    return app.send_static_file('index.html')

@app.route("/api/power/<speed>")
def power(speed):
    loaded_model = kr.models.load_model('model.h5')
    speed = float(speed)
    result = loaded_model.predict([speed])
    return jsonify({"value":result.item(0)})

if __name__ == "__main__":
    print("See README for instructions on running the application.")

