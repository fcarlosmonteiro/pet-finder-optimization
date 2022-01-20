import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sb

def compute_kde():
    '''
    Read the data into a pandas DataFrame
    Data with 68 points of missing pets
    Plot views from the dataset
    '''

    sb.set_style("white")
    plt.style.use("fivethirtyeight")

    dataset = pd.read_csv("dataset/dataset.csv")
    #print(dataset.describe())

    plt.figure(figsize=(12.75, 8))
    plt.plot([6.375, 6.375], [0, 8], "--", color="black", alpha=0.4, lw=1.25)

    
    #ploting all of the points according to the record that they came from.
    for month, group in dataset.groupby("Month"):
        plt.plot(group.X, group.Y, "o", label="Month %d" % (month))

    plt.xlim(0, 12.75)
    plt.ylim(0, 8)
    plt.xticks([])
    plt.yticks([])
    plt.legend(loc="upper center", ncol=7, frameon=True, fancybox=True, bbox_to_anchor=(0.5, 1.1))
    #plt.show();


    #computing a kernel density estimation (KDE) of the points, it can show us where a missing pet is most likely to appear.
    sb.kdeplot(dataset.X, dataset.Y, shade=True, cmap="Oranges")
    plt.plot([6.375, 6.375], [0, 8], "--", color="black", alpha=0.4, lw=1.25)
    plt.xlim(0, 12.75)
    plt.ylim(0, 8)
    plt.xlabel("")
    plt.ylabel("")
    plt.xticks([])
    plt.yticks([])
    plt.savefig('heatmap.png')
    #plt.show();
    
    return dataset

compute_kde()
