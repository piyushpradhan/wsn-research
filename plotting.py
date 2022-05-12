import matplotlib.pyplot as plt

def node_simulation(coord, s, d, r, chosen_path, population):
    """
    Simulate the nodes in the network
    """
    
    def each_line_plot(path):
        x_path = []
        y_path = []
        for i in path:
            x_path.append(i[0])
            y_path.append(i[1])
        return x_path, y_path
        
    plt.xlim = max(s[0], d[0])
    plt.ylim = max(s[1], d[1])

    x_axis = [s[0]]
    y_axis = [s[1]]
    axes = plt.subplot()
    for i in coord:
        x_axis.append(i[0])
        y_axis.append(i[1])
    x_axis.append(d[0])
    y_axis.append(d[1])

    x_path, y_path = each_line_plot(chosen_path)
    
    # plotting the position of nodes
    plt.scatter(x_axis, y_axis, s=10)

    # plotting the optimal path
    plt.plot(x_path, y_path, color='red', linewidth=2.0)

    # plotting the remaining paths
    for pop in population:
        pop_x_path, pop_y_path = each_line_plot(pop)
        plt.plot(pop_x_path, pop_y_path, linewidth=0.2)

    source = plt.Circle(s, r, fill=False)
    destination = plt.Circle(d, r, fill=False)
    axes.set_aspect(1)
    axes.add_artist(source)
    axes.add_artist(destination)
    plt.show()

def probability_simulation(p):
    x_axis = []
    for i in range(50):
        x_axis.append(i)
    y_axis = p
    plt.plot(x_axis, y_axis)
    plt.show()    