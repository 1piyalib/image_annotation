import matplotlib.pyplot as plt
import csv
import numpy as np


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

    pass

def show_annotation_graph():

    """
    Show scatter graph from files_and_bag.csv where x is index and y is annotation.  What happens when the first column is not a number
    """
    pass

def size_of_model_vs_annotation_graph():

  """
  read size_of_model vs annotation, plot scatter plot with 2 Y axis (or with two different colors)
  """

pass

def model_accuracy_graph():

    """
    add up the total amount of bags by reading through the csv file under bags_after_annotation and the amount you had to label, divide them to get accuracy
    """



if __name__ == "__main__":
    scatter_plot()