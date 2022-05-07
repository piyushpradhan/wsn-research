## Find forwarder
# Symbols used
# Notation Description 
# N Number of sensors 
# n Number of node in forward area
# R Transmission range 
# rk kth route
# Tk End-to-end delay of kth route 
# FZ Forward zone
# Ek Energy consumption of kth route 
# Rz Forward zone radius
# Pc (l), Connectivity probability 
# Ci A ith chromosome (path)
# Ed(y) Expected distance 
# E(Fi) Fitness function for energy consumption
# E(tcost). Expected computational cost 
# Etrans Transmission energy
# E(Etotal) Expected energy consumption
# Erec Receiving energy
# φ Density of sensors 
# PSD Probability of success delivery

import random
from wrt_polygon import *
from forward_zone_coord import *

def check_forward_zone(s, d, r, n, i): 
    """
    Check if the node is inside the forward zone
    """
    pass

def gen_coord(): 
    """
    Generate random coordinates which represent
    the location of sensor nodes scattered around
    """
    x = random.uniform(0, 9)
    y = random.uniform(0, 9)
    return (int(x), int(y))

def calc_dist(x, y): 
    """
    Calculate the distance between two sensor nodes
    """
    return ((x[0]-y[0])**2 + (x[1]-y[1])**2)**0.5

def find_forwarder(fz, s, d, r, n, forward_zone): 
    """
    Find the forwarder node
    """
    forwarder_list = []
    forwarder_node = ""
    for i in coord: 
        # add forward zone condition
        # check if i falls in FZ (the remaining condition)
        if calc_dist(s, i) <= r and (calc_dist(i, d) < calc_dist(s, d)) and is_inside_polygon(forward_zone, i):
            forwarder_list.append(i)
    if d in forwarder_list or len(forwarder_list) == 0:
        forwarder_node = d
    else: 
        forwarder_node = random.choice(forwarder_list)
    return forwarder_node

def chromosome_form(s, d, fz, r, n, forward_zone):
    """
    Generate a path for transmission of signal
    """
    chromosome = []
    chromosome.append(s)
    while s != d: 
        c2 = find_forwarder(fz, s, d, r, n, forward_zone)
        chromosome.append(c2)
        s = c2
    return chromosome

def population_form(s, d, fz, r, n, p, forward_zone):
    """
    Generate a population of paths
    """
    population = []
    for i in range(p):
        population.append(chromosome_form(s, d, fz, r, n, forward_zone))
    return population


if __name__ == "__main__": 
    n = 50
    s = [1, 3]
    d = [7, 8]
    r = 2
    coord = []
    while True:
        if len(coord) == n: 
            break
        new_coord = gen_coord()
        if new_coord not in coord:
            coord.append(gen_coord())
        else:
            pass
    forward_zone = point_of_intersection(r, s, d)
    forwarder = find_forwarder({1,2,3,4,5}, s, d, r, coord, forward_zone)
    # print(find_forwarder({1,2,3,4,5}, s, d, r, coord))
    population = population_form(s, d, {1,2,3,4,5}, r, coord, 10, forward_zone)

