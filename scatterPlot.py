import matplotlib.pyplot as plt
import csv
import numpy as np
import pandas as pd

def scatter_plot():
    plt.title("Random Scatter Plot") #title of scatter plot
    plt.xlabel("X values") #labels x values
    plt.ylabel("Y values") #labels y values

    filename = "csv_files\\example_scatter_data.csv"

    xval,yval,zval = np.loadtxt(filename, unpack = True, delimiter=',', skiprows=1)

    plt.scatter(xval,zval)
    plt.show()


def show_anotation_table():

    """
    Read files_and_bags.csv file and write them into a table
    look at table_from_csv() function in nasa code

    """
    # file_name = ""
    # filepath = "csv_files\\file_and_bags.csv"
    # file_name, bags, bags_after, changes = np.loadtxt(filepath, unpack = True, delimiter=',', skiprows=1)
    #
    # x = 0

    filepath = "csv_files\\file_and_bags.csv"
    df = pd.read_csv(filepath, sep=',')
    plt.table(cellText=df.values, colLabels=df.columns, loc='center')
    plt.show()


def show_annotation_graph():

    """
    Show scatter graph from files_and_bag.csv where x is index and y is annotation.
    What happens when the first column is not a number
    """
    filename = "files_and_bag.csv"

    xval, yval = np.loadtxt(filename, unpack=True, delimiter=',', skiprows=1)

    plt.scatter(xval, yval)
    plt.show()


def size_of_model_vs_annotation_graph():

  """
  read size_of_model_vs_annotation.csv, plot scatter plot with 2 Y axis (or with two different colors)
  """
  filename= "csv_files\\sizeof_model_vs_annotation.csv"
  xvals, oneline, secondline = np.loadtxt(filename, unpack=True, delimiter=',', skiprows=1)
  ax1 = plt.subplot()
  first, = ax1.scatter(oneline, color='red')
  ax2 = ax1.twinx()
  second, = ax2.scatter(secondline, color='orange')
  #the code below makes a legend so that you know which y value is which
  plt.legend([first, second], ["yval", "another yval"])


def model_accuracy_graph():

    """
    add up the total amount of bags by reading through the csv file under
    bags_after_annotation and the amount you had to label, divide them to get accuracy
    """
    import csv
    csv_file = csv.reader(open("file_and_bags.csv"))

    dist = 0
    for row in csv_file:
        _dist = row[2]
        try:
            _dist = float(_dist)
        except ValueError:
            _dist = 0

        dist += _dist




if __name__ == "__main__":
    #show_anotation_table()
    #show_annotation_graph()
    size_of_model_vs_annotation_graph()
