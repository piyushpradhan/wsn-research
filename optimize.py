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
from forward_zone_coord import *
from plotting import *

def gen_coord(s, d): 
    """
    Generate random coordinates which represent
    the location of sensor nodes scattered around
    """
    smallest_x = s[0]
    greatest_x = d[0]
    smallest_y = s[1]
    greatest_y = d[1]
    if s[0] > d[0]: 
        smallest_x = d[0]
        greatest_x = s[0]
    if s[1] > d[1]: 
        smallest_y = d[1]
        greatest_y = s[1]

    x = random.uniform(smallest_x, greatest_x)
    y = random.uniform(smallest_y, greatest_y)
    return (int(x), int(y))    

def calc_dist(x, y): 
    """
    Calculate the distance between two sensor nodes
    """
    return ((x[0]-y[0])**2 + (x[1]-y[1])**2)**0.5

def find_forwarder(s, d, r, coord, forward_zone): 
    """
    Find the forwarder node
    """
    forwarder_list = []
    forwarder_node = ()
    for i in coord: 
        if calc_dist(s, i) <= r and (calc_dist(i, d) < calc_dist(s, d)) and inside_polygon(forward_zone, i):
            forwarder_list.append(i)
    if d in forwarder_list or len(forwarder_list) == 0: 
        forwarder_node = d
    else: 
        forwarder_node = random.choice(forwarder_list)
    return forwarder_node

def chromosome_form(s, d, r, coord, forward_zone):
    """
    Generate a path for transmission of signal
    """
    chromosome = []
    chromosome.append(s)
    while s != d: 
        c2 = find_forwarder(s, d, r, coord, forward_zone)
        chromosome.append(c2)
        s = c2
    return chromosome

def population_form(s, d, r, coord, p, forward_zone):
    """
    Generate a population of paths
    """
    population = []
    for i in range(p):
        population.append(chromosome_form(s, d, r, coord, forward_zone))
    return population

def crossover(c1, c2):
    """
    Function to perform single point crossover
    """
    common_min = min(len(c1), len(c2))
    k = random.randint(0, common_min)
      
    # interchanging the genes
    for i in range(k, common_min):
        c1[i], c2[i] = c2[i], c1[i]
    return c1, c2

def calc_fitness(population, s, d, r, coord, forward_zone):
    """
    Calculate the fitness of each path
    """
    

if __name__ == "__main__": 
    n = 80
    s = (5, 8)
    d = (23, 32)
    r = 4
    coord = []
    while True:
        if len(coord) == n: 
            break
        new_coord = gen_coord(s, d)
        if new_coord not in coord:
            coord.append(gen_coord(s, d))
        else:
            pass
    forward_zone = point_of_intersection(r, s, d)
    chromosome_path = chromosome_form(s, d, r, coord, forward_zone)
    population = population_form(s, d, r, coord, 10, forward_zone)
    print("The initial population generated: ")
    for p in population:
        print(p)
    first_child, second_child = crossover(population[0], population[1])
    print("First child: ")
    print(first_child)
    print("Second child: ")
    print(second_child)
    node_simulation(coord, s, d, r)
    
