import os
import pandas
from methods.Matrix import plot_correlation_matrix
from methods.Density import plot_scatter_matrix
from methods.Histogram import plot_per_column_distribution
import matplotlib.pyplot as plt
from pathlib import Path
from obj.CustomDataFrame import CustomDataFrame


#   PATHS AND FILES
print(os.listdir('./input/sample_Signature/sample_Signature/forged/'))  # "." = in local directory search for "input"
forged_data_list = os.listdir('./input/sample_Signature/sample_Signature/forged/')  # creating a list of forged images
genuine_data_list = os.listdir('./input/sample_Signature/sample_Signature/genuine/')  # list of genuine images
image_dir_path = "./input/sample_Signature/sample_Signature/"
print(Path(image_dir_path).rglob('*.png'))
# end PATH AND FILES



d = {'genuine': genuine_data_list, 'forged': forged_data_list}
df = pandas.DataFrame(d)
cdf = CustomDataFrame(forged=forged_data_list, genuine=genuine_data_list, data_frame=df, forged_names=[], genuine_names=[])
print(cdf.data_frame, cdf.forged, cdf.genuine, cdf.genuine_names, cdf.forged_names, sep="\n")
#print(df)
string_df = df.to_string().split()
for i in range(0, len(string_df), 2):
    pass  # rewrite
print(string_df)


def support(cdf: CustomDataFrame, *args):
    """
    A method that runs on startup as loader. Should be used with check if files exist.
    :param cdf: custom data frame with provided paths and names
    :param args: some additional params. deprecated.
    :return: returns a matrix (must be a pandas dataset)
    """
    plot_correlation_matrix(df=cdf, graph_width=50)


support(cdf=cdf)


