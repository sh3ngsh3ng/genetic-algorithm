# Interesting problems to solve with this algo
# Set-cover, Travelling Salesman, Knapsack, Job scheduling, Vehicle Routing problems

# Main three processes
# 1) Reproduction: Generating new solutions from existing ones
# 2) Mutation: introducting random changes to diversify the population
# 3) Selection: Choosing which solutions survive and reproduce based on their fitness

# Example: One Max Problem
# [ _ _ _ _ _ ]
# [ 0 1 0 0 1 ] -> fitness = 2
# [ 1 1 1 1 1 ] -> fitness = 5

# Reproduction
# Crossover Method
# P1 => [ 1 1 1 : 0 0 0 0 ]
# P2 => [ 0 1 0 : 0 0 1 0 ]
# C1 => [ 1 1 1 0 0 1 0 ]
# C2 => [ 0 1 0 0 0 0 0 ]

# Mutation
# Randomly flipping 0 and 1s

import random
import numpy as np

POPULATION_SIZE = 1000
GENOME_LENGTH = 100
MUTATION_RATE = 0.01
CROSSOVER_RATE = 0.9
GENERATIONS = 500


def random_genome(length):
    return [random.randint(0, 1) for _ in range(length)]


def init_population(population_size, genome_length):
    return [random_genome(genome_length) for _ in range(population_size)]

def fitness(genome):
    return sum(genome)

def select_parent(population, fitness_values):
    total_fitness = sum(fitness_values)
    pick = random.uniform(0, total_fitness)
    current = 0
    for individual, fitness_value in zip(population, fitness_values):
        current += fitness_value
        if current > pick:
            return individual

def crossover(parent_one, parent_two):
    if random.random() < CROSSOVER_RATE:
        crossover_point = random.randint(0, len(parent_one) - 1)
        return parent_one[:crossover_point] + parent_two[crossover_point:], parent_two[:crossover_point] + parent_one[crossover_point:]
    else:
        return parent_one, parent_two


def mutate(genome):
    for i in range(len(genome)):
        if random.random() < MUTATION_RATE:
            genome[i] = abs(genome[i] - 1)
    return genome

def genetic_algorithm():
    population = init_population(POPULATION_SIZE, GENOME_LENGTH)
    for generation in range(GENERATIONS):
        fitness_values = [fitness(genome) for genome in population]

        new_population = []
        for _ in range(POPULATION_SIZE // 2):
            parent_one = select_parent(population, fitness_values)
            parent_two = select_parent(population, fitness_values)
            offspring_one, offspring_two = crossover(parent_one, parent_two)
            new_population.extend([mutate(offspring_one), mutate(offspring_two)])
        
        ### Replacing old population with new population
        population = new_population
        fitness_values = [fitness(genome) for genome in population]

        ### Combining old and new population
        # Evaluate fitness of the new population
        # fitness_values = [fitness(genome) for genome in new_population]
        # Combine the new population with the fittest individuals from the previous generation
        # combined_population = population + new_population
        # Select the fittest individuals for the next generation
        # population = [combined_population[i] for i in np.argsort(fitness_values)[-POPULATION_SIZE:]]

        best_fitness = max(fitness_values)
        # print(f"Generation {generation}: Best Fitness = {best_fitness}")
    
    best_index = fitness_values.index(max(fitness_values))
    best_solution = population[best_index]
    print(f'Best Solution: {best_solution}')
    print(f'Best Fitness: {fitness(best_solution)}')

if __name__ == "__main__":
    genetic_algorithm()




