# CA-02

# Install requirements
Python 3.13.1
all imports are at the beginning of the code and do not require additional installs

# Steps to run
code runs from top to bottom

# Narrative
The code begins with importing all nessesary libraries
the goal of the code is to seperate emails into spam emails or not spam emails
two functions are defined 
- one function to create a dictionary of the 3000 most common words in the emails
- one function to extract words from emails and assign those emails to spam or not spam

Afterward the data is brought in and the function are applied to test and train data seperatly

The results are vectorized and ran through 2 different naive bayes algorithums
GaussianNB and MultinomialNB

The results of each algorithums accuracy is displayed