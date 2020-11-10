# Disaster Response Pipeline Project

### Introduction

This project is focused on building an ETL pipeline for extracting , transforming and loading the disaster message data from Future Eight. 

Our goal here is to build a machine learning model to identify if these messages are related to disaster or not, and further label the nature of these messages. This would be of great help for some disaster relief agencies. We have 36 labels for these messages in total. Note, however, these labels are not mutually exclusive. Hence it is a multi-label classification problem.

The most obvious feature of those data messages is they are highly imbalanced. Several categories getting very few labels. To improve the accuracy, we implement a up-sample scheme before training.

After building and training such a model, we can next launch a web service which can label new messages from users' input.

### Instructions:
1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Run the following command in the app's directory to run your web app.
    `python run.py`

3. Go to http://0.0.0.0:3001/

### Software Packages

This project uses Python 3.7 and the following libraries:

NumPy
Pandas
nltk
scikit-learn
sqlalchemy


### Acknowledgment
Future Eight for the dataset
