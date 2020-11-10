# Disaster Response Pipeline Project

### Introduction

This project is focused on building an ETL pipeline for extracting , transforming and loading the disaster message data from Future Eight and then using that transformed and cleaned data to help build a Machine Learning model to help determine if a message can be classified into one of the categories of distater.

The model and the cleaned data are visualized using a flask web app. 

### Instructions:
1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Run the following command in the app's directory to run your web app.
    `python run.py`

3. Go to http://0.0.0.0:3001/ or https://view6914b2f4-3001.udacity-student-workspaces.com/

### Software Packages

This project uses Python 3.7 and the following libraries:

NumPy
Pandas
nltk
scikit-learn
sqlalchemy
plotly
flask


### Acknowledgment
Future Eight for the dataset
