import matplotlib.pyplot as plt

class Plot(): 
    def __init__(self, x, y, title, xlabel, ylabel): 
        self.x = x
        self.y = y 
        self.title = title 
        self.xlabel = xlabel 
        self.ylabel = ylabel

    def scatter_plot(self):
        """
        Plot a scatter plot
        """
        plt.scatter(self.x, self.y)
        plt.title(self.title)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.show()

    def line_plot(self):
        """
        Plot a line plot connecting the nodes
        """
        plt.plot(self.x, self.y)
        plt.title(self.title)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.show()