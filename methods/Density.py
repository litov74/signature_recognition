import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# Scatter and density plots
def plot_scatter_matrix(df, plot_size, text_size):
    df = df.select_dtypes(include=[np.number])  # keep only numerical columns
    # Remove rows and columns that would lead to df being singular
    df = df.dropna('columns')
    df = df[[col for col in df if df[col].nunique() > 1]]  # keep columns where there are more than 1 unique values
    column_names = list(df)
    if len(column_names) > 10:  # reduce the number of columns for matrix inversion of kernel density plots
        column_names = column_names[:10]
    df = df[column_names]
    ax = pd.plotting.scatter_matrix(df, alpha=0.75, figsize=[plot_size, plot_size], diagonal='kde')
    corrs = df.corr().values
    for i, j in zip(*plt.np.triu_indices_from(ax, k=1)):
        ax[i, j].annotate('Corr. coef = %.3f' % corrs[i, j], (0.8, 0.2), xycoords='axes fraction', ha='center',
                          va='center', size=text_size)
    plt.suptitle('Scatter and Density Plot')
    plt.show()
