import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
    Coffee_cups = []
    sleep_in_hours = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader :
            Coffee_cups.append(float(row['Coffee in ml']))
            sleep_in_hours.append(float(row['sleep in hours']))

    return{"x":Coffee_cups,"y":sleep_in_hours}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("correlation between Coffe in ml and Sleep time is ", correlation[0,1])


def setup():
    data_path = "Coffee Cups.csv"
    dataSource = getDataSource(data_path)
    findCorrelation(dataSource)


setup()
