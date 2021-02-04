import pandas as pd
import sweetviz as sv
import time 


# Creating a report is a quick 3-line process:
# Create a Pandas dataframe
# upload = pd.read_csv('marketing_data.csv')
# Create a copy of the DataFrame to work from
# data = upload.copy()
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

def switchDataFrame(Training_set_csv:str, Testing_set_csv:str):
    """
    Invoke function to use time as an idicator for whether to launch HTML
    User Interface    SweetViz html page.
    """
    # Establish criteria for time
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    current_min = current_time[3:5]
    print(current_time)
        
    training_set = pd.read_csv(Training_set_csv)
    testing_set = pd.read_csv(Testing_set_csv)
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
