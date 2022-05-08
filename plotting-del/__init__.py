from plotting.plot import Plot
from optimize import *

def main():
    # plot = Plot([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], "Scatter Plot", "X", "Y")
    # plot.scatter_plot()

    pass

def node_simulation(coord):
    # Generate a scatter plot for the available nodes
    nodes = coord
    x_axis = []
    y_axis = []
    for i in coord:
        x_axis.append(i[0])
        y_axis.append(i[1])
    plot = Plot(x_axis, y_axis, "Scatter Plot", "X", "Y")
    plot.scatter_plot()
    line_plot = Plot(x_axis[0:4], y_axis[0:4], "Line plot", "X", "Y")
    line_plot.line_plot()