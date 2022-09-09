from haversine import haversine

def calculate_distance(lat1, long1, lat2, long2):
    """
        Returns the distance in km between the points
    """
    loc1 = (lat1,long1)
    loc2 = (lat2,long2)
    return haversine(loc1,loc2)

def compute_fitness(solution,pet_location_map):
    """
        Computes the fitness function. GA tries minimize this function, so, a lower distance is better to solve the problem.
        Analyzes the distance between the coordinates pair by pair.
    """
    fitness = 0.0
    for index in range(1, len(solution)):
        w1 = solution[index]
        w2 = solution[index - 1]
        fitness += calculate_distance(pet_location_map[w1][0], pet_location_map[w1][1], pet_location_map[w2][0], pet_location_map[w2][1])
    
    print("solução = ", solution, "fitness =" ,fitness)    
    return fitness