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

import sys
from math import e, factorial

import random

from torch import randint
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

def gen_random_coords(s, d, n):
    """
    Compiles the randomly generated coordinates
    """
    coord = []
    while True:
        if len(coord) == n: 
            break
        new_coord = gen_coord(s, d)
        if new_coord not in coord:
            coord.append(gen_coord(s, d))
        else:
            pass
    return coord

def calc_dist(x, y): 
    """
    Calculate the distance between two sensor nodes
    """
    return ((x[0]-y[0])**2 + (x[1]-y[1])**2)**0.5

def count_nodes_inside_forward_zone(coord, forward_zone):
    """
    Return the number of nodes inside the forward zone
    """
    count = 0
    for i in range(len(coord)): 
        if inside_polygon(forward_zone, coord[i]):
            count = count + 1
    return count

def find_forwarder(s, d, r, coord, forward_zone): 
    """
    Find the forwarder node
    """
    forwarder_list = []
    forwarder_node = ()
    for i in coord: 
        # the condition for finding the next best node for the path
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
    # creating a path
    # adding nodes to an array (the path) till the destination node is reached
    while s != d: 
        c2 = find_forwarder(s, d, r, coord, forward_zone)
        if c2 == ():
            break
        chromosome.append(c2)
        s = c2
    return chromosome

def population_form(s, d, r, coord, p, forward_zone):
    """
    Generate a population of paths
    """
    population = []
    for i in range(p):
        path = chromosome_form(s, d, r, coord, forward_zone)
        in_range = calc_dist(path[-2], d) <= r
        if in_range == False:
            return False
        else: 
            population.append(path)

    return population

# def crossover(c1, c2):
#     """
#     Function to perform single point crossover
#     """
#     common_min = min(len(c1), len(c2))
#     k = random.randint(0, common_min)
      
#     # interchanging the genes
#     for i in range(k, common_min):
#         c1[i], c2[i] = c2[i], c1[i]
#     children = [c1, c2]
#     return children

def crossover(c1, c2):
    """
    Perform single point crossover operation
    """
    if len(c1) != len(c2):
        return [c1, c2]
    length = len(c1)
    if length < 2:
        return [c1, c2]

    p = randint(low=1, high=length - 1)
    children = [c1[0:p] + c2[p:], c2[0:p] + c1[p:]]
    return children

def calc_fitness(path):
    """
    Calculate and return the fitness of each path
    """
    # energy dissipated to run the transmitter
    elec = 50
    # energy required to for transmit amplifier
    amp = 100
    # value usually lies between the range of 2 to 4
    phi = 2
    # bits of data to be trasnferred
    k = 512
    # number of links along the route from S to D
    hc = len(path) - 1
    total_energy = 0
    
    for i in range(len(path) - 1):
        current_energy = (2 * elec * amp * (calc_dist(path[i], path[i + 1]) ** phi)) * k * hc
        total_energy = total_energy + current_energy
    
    return total_energy

def forward_zone_probability(n, r, d):
    """
    Calculate and return the probability of n nodes in forward zone
    """
    phi = 2 
    area = 2 * r * d
    probability = ((phi * area) ** 34) / (factorial(n) * (phi ** n))
    return probability

def run_simulation(): 
    n = 200
    s = (5, 8)
    d = (23, 32)
    r = 4
    coord = gen_random_coords(s, d, n)
    
    # defines the forward zone
    forward_zone = point_of_intersection(r, s, d)
    # one of the possilble paths to go from S to D
    chromosome_path = chromosome_form(s, d, r, coord, forward_zone)
    # generate the initial population for crossover
    population = population_form(s, d, r, coord, 60, forward_zone)
    while(population == False):
        coord = gen_random_coords(s, d, n)
        population = population_form(s, d, r, coord, 60, forward_zone)

    # count the number of nodes inside the forward zone
    count = count_nodes_inside_forward_zone(coord, forward_zone)

    # calculate the probability of n nodes in forward zone
    p = []
    probability_fz = forward_zone_probability(count, r, calc_dist(s, d))
    print(f"Probability of {count} nodes lying inside forward zone: {probability_fz % e ** (-1)}")
    for nodes in range(50):
        prob = forward_zone_probability(nodes, r, calc_dist(s, d)) % e ** (-1)
        p.append(prob)
        print(prob)
    # probability_simulation(p)

    optimal = []
    optimal_fitness = sys.maxsize
    for i in range(len(population)):
        fitness_value = calc_fitness(population[i])
        if fitness_value < optimal_fitness: 
            optimal_fitness = fitness_value
            optimal = population[i]
    
    print(optimal)
    node_simulation(coord, s, d, r, optimal, population)
    
    # Create simulation with crossover operation
    offspring = population
    chosen_path = []
    gen_lowest = sys.maxsize
    gen_count = 0
    final_population_count = 0
    
    for gen in range(10):
        # print("Generation: ", gen)
        # print("The fitness values are: ", end="")
        population_lowest = sys.maxsize
        population_count = 0
        pop_chosen_path = []
        for i in range(len(offspring)): 
            # proves that the fitness values actually are different
            # print("path: ", offspring[i], " fitness: ", calc_fitness(offspring[i]), end="\n")
            fitness_value = calc_fitness(offspring[i])
            if fitness_value < population_lowest: 
                population_count = i
                population_lowest = fitness_value
                pop_chosen_path = offspring[i]
                # print(f"Lowest in {gen} generation: {i} population -> {gen_count}:{population_count}")
            
        # print(fitness_values)
        # print("The lowest fitness value of population is: ", population_lowest)
        if population_lowest < gen_lowest:
            gen_count = gen
            final_population_count = population_count
            gen_lowest = population_lowest
            chosen_path = pop_chosen_path
            # print(f"Chosen path so far: {chosen_path}")
            # print(f"Lowest so far : {gen_count}:{population_count}")
            # print(f"Lowest fitness value so far: {gen_lowest}")
        
        offspring = crossover(offspring[0], offspring[1])
        
    # print("The lowest fitness value (overall) is: ", gen_lowest, "from: ", gen_count, " generation's ", final_population_count, " population")
    # print(f"The chosen path: {chosen_path}")
    # print(f"Fitness value of chosen path: {calc_fitness(chosen_path)}")

    # node_simulation(coord, s, d, r, chosen_path)
    
run_simulation()