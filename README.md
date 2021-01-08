# EmergingTechProject
This Repository was created by Steven Joyce, a 4th year GMIT student for the Emerging Technology Project.
# Project Instructions
Instructions
In this project you must create a web service that uses machine learning to make predictions based on the data set powerproduction available on Moodle. The goal is to produce a model that accurately predicts wind turbine power output from wind speed
values, as in the data set. You must then develop a web service that will respond with predicted power values based on speed values sent as HTTP requests. Your submissionmust be in the form of a git repository containing, at a minimum, the following items:
1. Jupyter notebook that trains a model using the data set. In the notebook you should explain your model and give an analysis of its accuracy.
2. Python script that runs a web service based on the model, as above.
3. Dockerfile to build and run the web service in a container.
4. Standard items in a git repository such as a README.

## Repository contents
This repository contains several files. Listed below are the files and their functions;
```static``` - Inside is the HTML file called index.html for running the webservice.py in a web application.
```model.ipynb``` - The code to fun the dataset in a model is created in here. 
```Dockerfile``` - File contains compilation instructions for a Docker image.
```.datamodel.h5``` - This file contains a copy of the model created in model.ipynb to be used in webservice.py.
```.powerproduction.csv``` - The csv file that has the dataset used in the model.ipynb file code.
```README.md``` - Contains all information about the project.
. ```webservice.py``` - A Flask application that uses the model stored in the datamodel.h5 file to generate a prediction with user input.
10. ```wind_turbine_training_models.ipynb``` - A Juptyer notebook that inports the powerproduction.csv file to create and export a keras/tensorflow model called "wind_turbine_model".

## System Requirements
numpy==1.19.2
Flask==1.1.2
tensorflow==2.4.0
sklearn
matplotlib == 3.3.2
pandas == 1.1.3

## Run the flask application in webservice.py
Make sure all requirements are installed before running the following code lines in the command line
### Linux
1. ```export FLASK_APP=webservice.py```
2. ```python3 -m flask run```

### Windows
1. ```set FLASK_APP=webservice.py```
2. ```python -m flask run```

## How to Build, Run, Kill and Remove a Docker Image.
1. Build the Docker image: ```docker build -t web-service .```
2. Run the Docker image: ```docker run -d -p 5000:5000 web-service```
3. Check running Docker images: ```docker container ls```
4. Kill a runner instance of a Docker image: ```docker kill CONTAINER_ID```
5. Remove a Docker image: ```docker rm CONTAINER_ID```
