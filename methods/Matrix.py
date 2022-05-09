import matplotlib.pyplot as plt


# Correlation matrix
import pandas

from obj import CustomDataFrame


def plot_correlation_matrix(df: CustomDataFrame, graph_width):
    #filename = df.dataframeName
    df = df.data_frame.dropna('columns')  # drop columns with NaN
    df = df.data_frame[[col for col in df.data_frame if df.data_frame[col].nunique() > 1]]  # keep columns where there are more than 1 unique values
    if df.data_frame.shape[1] < 2:
        print(f'No correlation plots shown: The number of non-NaN or constant columns ({df.data_frame.shape[1]}) is less than 2')
        return
    corr = df.data_frame.corr()
    plt.figure(num=None, figsize=(graph_width, graph_width), dpi=80, facecolor='w', edgecolor='k')
    corr_mat = plt.matshow(corr, fignum=1)
    plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
    plt.yticks(range(len(corr.columns)), corr.columns)
    plt.gca().xaxis.tick_bottom()
    plt.colorbar(corr_mat)
    plt.title(f'Correlation Matrix for filename', fontsize=15)
    #plt.title(f'Correlation Matrix for {filename}', fontsize=15)
    plt.show()
