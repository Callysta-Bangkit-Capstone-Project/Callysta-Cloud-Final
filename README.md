# Bangkit-C22CB-Company-Based-Capstone


This is our repository for Company Based Capstone.

Our team Consist of 6 people.

- [Bangkit-C23-PS363-Company-Based-Capstone](#bangkit-c23-ps363-company-based-capstone)
  - [Members](#members)
  - [What is this?](#what-is-this)
  - [Getting started](#getting-started)
  - [Deployment to app engine](#deployment-to-app-engine)
  - [Deployment ML model to Cloud Function](#deployment-ml-model-to-cloud-function)

## Members

Name | Bangkit ID | Learning Path | Github Profile
:---|:---:|:---:|---:
Ega Fernanda Putra | M038DSX0496 | Machine Learning | [Profile](https://github.com/Fallennnnnn)
Muhammad Raffi Priyadiantama| M038DSX0498 | Machine Learning | [Profile](https://github.com/Raffi-072)
Muhammad Naufal A. |  A013DSX2909 | Mobile Development | [Profile](https://github.com/mhmmdnaufall)
Danil Ardi | A013DSX0990 | Mobile Development | [Profile](https://github.com/danilardi)
Ridho Kartoni Pasaribu | C013DSX0978 | Cloud Computing | [Profile](https://github.com/ridhokartoni)
Ruben Tricahya Boediono | C038DSX0600 | Cloud Computing | [Profile](https://github.com/rubenboediono)


## What is this? 

This repository contains a Flask API that is deployed on Google App Engine. The API provides functionality for interacting with the specified endpoints using HTTP requests. The code is built with Python and utilizes the Flask web framework.

## Getting started

1. Clone the repository to your local machine
```bash
git clone https://github.com/Callysta-Bangkit-Capstone-Project/Callysta-CloudComputing.git

```
2. Navigate to the project directory:
```bash
cd Callysta-CloudComputing

```
3. Create a virtual environment to isolate the project dependencies:
```bash
python -m venv callysta-env

```
4. Activate the virtual environment
On MacOs/Linux
```bash
source callysta-env/bin/activate

```
On Windows
```bash
callysta-env/Scripts/activate

```
5. Install the required dependencies by running the following command
```bash
pip install -r requirements.txt

```
6. Set up the necessary configurations for deploying to Google App Engine. Make sure you have a Google Cloud Platform project with the App Engine service enabled.

7. Modify the app.yaml file to configure the App Engine deployment settings, such as the runtime, environment variables, and other configurations specific to your application.

8. Run the Flask API locally by executing the following command:
```bash
python main.py

```
9. This will start the development server at http://localhost:8080/.

## Deployment to App Engine
1. Ensure you have the Google Cloud SDK installed on your machine.

2. Set up your Google Cloud project and configure the project ID:
```bash
gcloud config set project PROJECT_ID

```
3.  Deploy the application to App Engine using the following command:
```bash
gcloud app deploy

```

4. Once the deployment is complete, you can access your API at 
https://YOUR_PROJECT_ID.uc.r.appspot.com/

## Deployment ML model to Cloud Function
1. Create a new Cloud Function in your Google Cloud project. Make sure you have the Cloud Functions API enabled
2. Write a new function in the Cloud Function that will handle the prediction request from your Flask API
3. Within the Cloud Function, load your trained machine learning model
4. Implement the necessary code to preprocess the incoming request data from your Flask API and pass it to your machine learning model for prediction. Ensure that the response from the model is properly formatted for the API response
5. Deploy the Cloud Function by running the deployment command specific to your cloud environment
```bash
gcloud functions deploy function-name --runtime RUNTIME --trigger-http

```
Replace function-name with the name you want to give to your Cloud Function and RUNTIME with the language or runtime you're using (e.g., python3.9).
6. Once the Cloud Function is deployed, take note of the generated URL endpoint for the function


