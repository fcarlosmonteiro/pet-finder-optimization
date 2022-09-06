from __future__ import print_function
#from data_view import compute_kde
import map_manipulation
import matplotlib.pyplot as plt
import pandas as pd
import math
import random

db = pd.read_csv("/home/fcarlos/Documentos/Projetos-Git/pet-finder-optimization/dataset/dataset_DV.csv")
mp = map_manipulation.Create_Maps()
pet_location_map = {}

for i, record in db.iterrows():
    key = "M%dD%d" % (record.Month, record.Day)
    pet_location_map[key] = (record.X, record.Y)
#print(pet_location_map)
    
def calculate_distance(x1, y1, x2, y2):
    """
        Returns the Euclidean distance between the points
    """
    return math.sqrt( (x2 - x1)**2 + (y2 - y1)**2 )

def compute_fitness(solution):
    """
        Computes the fitness function. GA tries minimize this function, so, a lower distance is better to solve the problem.
        Analyzes the distance between the coordinates pair by pair.
    """
    fitness = 0.0
    #print("sol:", solution)
    for index in range(1, len(solution)):
        w1 = solution[index]
        w2 = solution[index - 1]
        print(w1,w2)
        fitness += calculate_distance(pet_location_map[w1][0], pet_location_map[w1][1], pet_location_map[w2][0], pet_location_map[w2][1])
        
    return fitness

def generate_random_individual():
    """
        Creates a random path.
    """
    new_random_individual = list(pet_location_map.keys())
    random.shuffle(new_random_individual)
    return tuple(new_random_individual)

def crossover(indiv_genome, max_points=3):
    """
        Uses the max_points parameter to select the crossover points to the individual.     
        A point swaps the order of two locations in the path.
    """
    indiv_genome = list(indiv_genome)
    num_mutations = random.randint(1, max_points)
    
    for mutation in range(num_mutations):
        swap_index1 = random.randint(0, len(indiv_genome) - 1)
        swap_index2 = swap_index1

        while swap_index1 == swap_index2:
            swap_index2 = random.randint(0, len(indiv_genome) - 1)

        indiv_genome[swap_index1], indiv_genome[swap_index2] = indiv_genome[swap_index2], indiv_genome[swap_index1]
            
    return tuple(indiv_genome)

def shuffle_mutation(indiv_genome):
    """
        Applies a single shuffle mutation to the individual, it moves a random part of the path to another location.
    """
    indiv_genome = list(indiv_genome)
    
    start_index = random.randint(0, len(indiv_genome) - 1)
    length = random.randint(2, 20)
    
    genome_subset = indiv_genome[start_index:start_index + length]
    indiv_genome = indiv_genome[:start_index] + indiv_genome[start_index + length:]
    
    insert_index = random.randint(0, len(indiv_genome) + len(genome_subset) - 1)
    indiv_genome = indiv_genome[:insert_index] + genome_subset + indiv_genome[insert_index:]
    
    return tuple(indiv_genome)

def generate_random_population(pop_size):
    """
        Generates a list with `pop_size` number of random individuals.
    """
    random_population = []
    for agent in range(pop_size):
        random_population.append(generate_random_individual())
    return random_population

def plot_trajectory(indiv_genome):
    """
        Create a visualization of the given path.
    """
    lat = []
    long = []
    agent_fitness = compute_fitness(indiv_genome)

    for pet_loc in indiv_genome:
        lat.append(pet_location_map[pet_loc][0])
        long.append(pet_location_map[pet_loc][1])

    mp.mark_points(lat,long)
    mp.plot_route(lat,long)

    plt.figure()
    plt.title("Fitness: %f" % (agent_fitness))
    plt.plot(lat[:18], long[:18], "-o", markersize=7)
    plt.plot(lat[17:35], long[17:35], "-o", markersize=7)
    plt.plot(lat[34:52], long[34:52], "-o", markersize=7)
    plt.plot(lat[51:], long[51:], "-o", markersize=7)
    plt.plot(lat[0], long[0], "^", color="#1f77b4", markersize=15)
    plt.plot(lat[-1], long[-1], "v", color="#d62728", markersize=15)
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])
    #plt.show()
    plt.savefig('fit.png')


def run_genetic_algorithm(generations, population_size):
    """
        The main method of Genetic Algorithm.
        
        `generations` and `population_size` must be a multiple of 10.
    """
    
    population_subset_size = int(population_size / 10.)
    generations_10pct = int(generations / 10.)
    
    # Create an initial random population.
    population = generate_random_population(population_size)

    # number of GA repetitions 
    for generation in range(int(generations)):
        
        # Compute the fitness function for the current population
        population_fitness = {}

        for individual in population:
            if individual in population_fitness:
                continue

            population_fitness[individual] = compute_fitness(individual)

        # Take the top 10% shortest paths and produce offspring from each of them
        new_population = []
        for rank, individual in enumerate(sorted(population_fitness,
                                                   key=population_fitness.get)[:population_subset_size]):

            if (generation % generations_10pct == 0 or generation == (generations - 1)) and rank == 0:
                #pass
                print("Generation %d best: %f" % (generation, population_fitness[individual]))
                print(individual)
                plot_trajectory(individual)

            # Create 1 exact copy of each top path
            new_population.append(individual)

            # Create 4 offspring with 1-3 mutations
            for offspring in range(4):
                new_population.append(crossover(individual, 3))
                
            # Create 5 offspring with a single shuffle mutation
            for offspring in range(5):
                new_population.append(shuffle_mutation(individual))

        # Replace the old population with the new population of offspring
        for i in range(len(population))[::-1]:
            del population[i]

        population = new_population
        
run_genetic_algorithm(generations=100, population_size=50)