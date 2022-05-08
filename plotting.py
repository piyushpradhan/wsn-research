import matplotlib.pyplot as plt

def node_simulation(coord, s, d, r):
    """
    Simulate the nodes in the network
    """
    x_axis = [s[0]]
    y_axis = [s[1]]
    axes = plt.subplot()
    for i in coord:
        x_axis.append(i[0])
        y_axis.append(i[1])
    x_axis.append(d[0])
    y_axis.append(d[1])

    plt.ylim((0, 50))
    plt.xlim((0, 50))
    plt.scatter(x_axis, y_axis)
    source = plt.Circle(s, r, fill=False)
    destination = plt.Circle(d, r, fill=False)
    axes.set_aspect(1)
    axes.add_artist(source)
    axes.add_artist(destination)
    plt.show()
    