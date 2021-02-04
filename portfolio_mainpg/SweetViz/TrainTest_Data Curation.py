import pandas as pd
import sweetviz as sv
import time 


# Creating a report is a quick 3-line process:
# Create a Pandas dataframe
training_upload = pd.read_csv('portfolio_mainpg\SweetViz\Training_Set.csv')
testing_upload = pd.read_csv('portfolio_mainpg\SweetViz\Testing_Set.csv')
# Create a copy of the DataFrame to work from
training_set = training_upload.copy()
testing_set = testing_upload.copy()
# Omit random state to have different random split each run
# training_set = data.sample(frac=0.75, random_state=0)
# testing_set = data.drop(training_set.index)

# # (Optional) Visualize the Train/Split
# print('Training set', train_set.shape)
# print(train_set.head(5))  # See five rows
# print('\nTest set', test_set.shape)
# print(test_set.head(5))  # See five rows
# print('\nOriginal DataFrame', data.shape)
# print(data.head(5))  # See five rows

# (Optional) Save Train and Test Dataframe
# training_set.to_csv('Training_Set.csv')
# testing_set.to_csv('Testing_Set.csv')

def switchDataFrame(training_set, testing_set):
    """
    Invoke function to use time as an idicator for whether to launch HTML
    User Interface    SweetViz html page.
    """
    # Establish criteria for time
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    current_min = current_time[3:5]
    print(current_time)
        
    if (int(current_min) % 2) == 0:  # Even minutes
        try:
            training_report = sv.analyze(training_set)
            training_report.show_html()
        except:
            RuntimeError
    if (int(current_min) % 2) != 0:  # Odd minutes
        try:
            testing_report =sv.analyze(testing_set)
            testing_report.show_html()
        except:
            RuntimeError


switchDataFrame(training_set, testing_set)
