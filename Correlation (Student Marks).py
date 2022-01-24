import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
    student_marks = []
    student_days = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader :
            student_marks.append(float(row['Marks In Percentage']))
            student_days.append(float(row['Days Present']))

    return{"x":student_marks,"y":student_days}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("correlation between Student Marks and Days Present are ", correlation[0,1])


def setup():
    data_path = "Student Marks.csv"
    dataSource = getDataSource(data_path)
    findCorrelation(dataSource)


setup()
