import os

import pandas

import methods.Matrix
from methods.Matrix import plot_correlation_matrix
from methods.Density import plot_scatter_matrix
from methods.Histogram import plot_per_column_distribution
import matplotlib.pyplot as plt
from pathlib import Path


print(os.listdir('./input/sample_Signature/sample_Signature/forged/'))  # "." = in local directory search for "input"
forged_data_list = os.listdir('./input/sample_Signature/sample_Signature/forged/')  # creating a list of forged images
genuine_data_list = os.listdir('./input/sample_Signature/sample_Signature/genuine/')  # list of genuine images
image_dir_path = "./input/sample_Signature/sample_Signature/"
print(Path(image_dir_path).rglob('*.png'))
d = {'genuine': genuine_data_list, 'forged': forged_data_list}
df = pandas.DataFrame(d)
print(df)
string_df = df.to_string().split()
for i in range(0, len(string_df), 2):
    pass  # rewrite
print(string_df)


def support(data: list = [], df: pandas.DataFrame = pandas.DataFrame(), *args):
    """
    A method that runs on startup as loader. Should be used with check if files exist.
    :param df: a dataFrame type from pandas.
    :param data: a list with images addresses.
    :return: returns a matrix (must be a pandas dataset)
    """
    #for i in range(0, len(data)):
    #    image = open("./input/sample_Signature/sample_Signature/forged/" + data[i], "r")
    #    df.dataframeName = data[i]
    #    print(image.name, image.mode)  # debug only
    #    plot_correlation_matrix(df, 50)
    plot_correlation_matrix(df=df, graph_width=50)



#support()

