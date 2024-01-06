import random
import numpy as np

def calculate_higher_fitness(parent1_fitness, parent2_fitness, child_fitness):
    if child_fitness > parent1_fitness and child_fitness > parent2_fitness:
        return 0
    elif parent2_fitness < child_fitness < parent1_fitness or child_fitness < parent2_fitness < parent1_fitness:
        return 1
    elif parent1_fitness < child_fitness < parent2_fitness or child_fitness < parent1_fitness < parent2_fitness:
        return 2

def create_random_cities(num_cities):
   return np.random.rand(num_cities, 4)

def calculate_distance(city1, city2):
   return np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def fitness(route, cities):
   total_distance = 0
   for i in range(len(route) - 1):
       total_distance += calculate_distance(cities[route[i]], cities[route[i + 1]])
   return total_distance

def create_initial_population(pop_size, num_cities):
    population = []
    for _ in range(pop_size):
        route = [0]
        route.extend(random.sample(range(1, num_cities), num_cities - 1))
        route.append(0)
        population.append(route)
    return population


def crossover(parent1, parent2):
   child = [-1] * (len(parent1)-1)
   child[0] = 0
   child.append(0)
   start, end = sorted(random.sample(range(1,len(parent1)-1), 2))
   child[start:end] = parent1[start:end]
   for city in parent2:
       if city not in child:
           for i in range(len(child)):
               if child[i] == -1:
                   child[i] = city
                   break
   return child

def mutate(route, mutation_rate):
   for i in range(1,len(route)-1):
        if random.random() < mutation_rate:
            swap_with = random.randint(1, len(route) - 1)
            route[i], route[swap_with] = route[swap_with], route[i]
   return route






num_cities = 15
pop_size = 10
mutation_rate = 0.01
iter_count = 100






cities = create_random_cities(num_cities)
population = create_initial_population(pop_size, num_cities)


print("\nİlk Popülasyon\n")
for route in population:
    print(route,fitness(route, cities))

distances = []
for item in population:
    distances.append(fitness(item, cities))

min_dist = min(distances)
print('\nMinimum Total Distance',min_dist)




for j in range(iter_count):
    
    pop_selection = list(range(pop_size))
    
    for i in range(0,len(population),2):
        parent1_index = int(np.random.rand()*len(pop_selection))
        pop_selection.pop(parent1_index)
        parent2_index = int(np.random.rand()*len(pop_selection))
        pop_selection.pop(parent2_index)
        
        parent1, parent2 = population[parent1_index], population[parent2_index]
        child = crossover(parent1, parent2)
        mutated_child = mutate(child, mutation_rate)
        route_fitness = fitness(mutated_child, cities)
        parent1_fitness = fitness(parent1, cities)
        parent2_fitness = fitness(parent2, cities)
        change_index = calculate_higher_fitness(parent1_fitness, parent2_fitness, route_fitness)
        if change_index == 1:
            population[parent1_index] = mutated_child
        elif change_index == 2:
            population[parent2_index] = mutated_child
    
    distances = []
    for item in population:
        distances.append(fitness(item, cities))
    if min_dist > min(distances):
        min_dist = min(distances)
        
        print("\n******************************\n")
        print(str(j+1)+". İterasyon\n")
        for route in population:
            print(route," T.Distance: ",fitness(route, cities))
        print("\nYeni Minimum Total Distance:",min_dist)
        
    






















