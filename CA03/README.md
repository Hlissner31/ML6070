### Decision Tree Classifier - Income Prediction

# Overview

This Jupyter Notebook implements a Decision Tree Classifier to predict whether an individual's income is <=50K or >50K based on various socio-economic factors. It includes data preprocessing, model training, hyperparameter tuning, and predictions using the best-performing model.

# Dataset

The dataset contains demographic and work-related attributes, such as:

Hours Worked per Week

Occupation Category

Marriage Status & Relationships

Capital Gain

Race-Sex Group

Number of Years of Education

Education Category

Work Class

Age

Source

The dataset is loaded from: (https://github.com/ArinB/MSBA-CA-03-Decision-Trees/blob/master/census_data.csv?raw=true)

Installation & Requirements

To run this notebook, you need the following Python libraries:

pip install pandas numpy scikit-learn matplotlib seaborn autoviz

Running the Notebook

Open the Jupyter Notebook:

jupyter notebook HL_CA-03.ipynb

Run all cells in sequence:

Load the dataset

Perform exploratory data analysis

Preprocess the data (encoding & binning)

Train a Decision Tree model

Tune hyperparameters

Evaluate model performance

Make a final prediction on new data

Prediction Task

The notebook predicts an individual's income category based on input features. To test the model, a sample individual's data is used:

new_data = {
    'Hours Worked per Week': [48],
    'Occupation Category': ['Mid - Low'],
    'Marriage Status & Relationships': ['High'],
    'Capital Gain': ['Yes'],
    'Race-Sex Group': ['Mid'],
    'Number of Years of Education': [12],
    'Education Category': ['High'],
    'Work Class': ['Income'],
    'Age': [58]
}

The trained model predicts whether the individual's income is <=50K or >50K.

Results

The best-performing Decision Tree model is selected based on accuracy, precision, recall, and F1-score. The final model is used to predict income for new data.