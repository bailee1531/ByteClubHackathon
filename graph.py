import pandas as pd
import matplotlib.pyplot as plt

filename = input("Enter the name of the file you want to create graphs for: ")

df = pd.read_csv(filename)

graph_num = int(input("# of graphs: "))
fig, ax = plt.subplots(1, graph_num)

for i in range(0, graph_num):
    x_axis = input("Enter the x-axis: ")
    y_axis = input("Enter the y-axis: ")
    ax[i].plot(df[x_axis], df[y_axis])
    ax[i].set_xlabel(x_axis)
    ax[i].set_ylabel(y_axis)
    ax[i].set_title(y_axis + " vs " + x_axis)

plt.grid(True)
plt.show()