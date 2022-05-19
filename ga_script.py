import numpy
import ga

# Inputs of the equation (most probably the parameters)
equation_inputs = [4, -2, 3.5, 5, -11, -4.7]

# number of weights we are looking to optimize
num_weights = 6

sol_per_pop = 8

# The population will have sol_per_pop chromosomes where each chromosome has num_weights genes
pop_size = (sol_per_pop, num_weights)

# Generating the initial population 
new_population = numpy.random.uniform(low=-4.0, high=4.0, size=pop_size)

print("Population Generated:")
print(new_population)

num_generations = 5
num_parents_mating = 4

for generation in range(num_generations): 
    # Measuring the fitness value of each chromosome
    fitness = ga.cal_pop_fitness(equation_inputs,  new_population)
    # Selecting the best parents in the population for mating 
    parents = ga.select_mating_pool(new_population, fitness, num_parents_mating)

    # Generating the next generation using crossover
    offspring_crossover = ga.crossover(parents, offspring_size=(pop_size[0] - parents.shape[0], num_weights))

    # Adding some variations to the offspring using mutation
    offspring_mutation = ga.mutation(offspring_crossover)

    # Creating the new population based on the parents and offspring
    new_population[0:parents.shape[0], :]  = parents
    new_population[parents.shape[0]:, :] = offspring_mutation

print("New population: ")
print(new_population)


