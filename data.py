"""
data.py: Function to load training data on student statistics for taking quizzes.

Function:
    - load_student_data(): Reads a CSV file into a DataFrame and returns it.
"""

import pandas as pd

def load_student_data():
    return pd.read_csv('dataset/student_statistics.csv')
