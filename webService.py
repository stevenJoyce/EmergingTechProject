# import the flask web service
import flask as fk

# Create a new web app.
app = fk.Flask(__name__)

# Add route to the root ('/') location, that calls the "hello_world()" function.
@app.route('/')
def hello_world():
    return "Hello world!"

