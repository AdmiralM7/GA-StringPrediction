import random
import math

# fitness function : depends on number of characters that are in right place (optimized)
def fitness_fn(chromosome):
    fitness = 0.0
    for i in range(len(target)):
        if target[i] == chromosome[i]:
            fitness += 1
        elif chromosome[i] in target:
            if chromosome.count(chromosome[i]) == target.count(chromosome[i]):
                fitness += 0.1
            '''else:
                fitness += 0.05'''
    result = math.pow(2,fitness)
    return result

# Mutation function : changes one character from Chromosome (3% chance)
def mutate(chromosome):
    if random.random() <= mutation_rate:
        index = random.randint(0,len(chromosome)-1)
        chromosome = chromosome[:index] + random.choice(letters) + chromosome[index+1:]
    return chromosome
    

# Crossover function :  slice 2 Chromosomes and merge them to get child
def crossover(chromosome1,chromosome2):
    index = random.randint(1,len(target)-1)
    result = chromosome1[:index] + chromosome2[index:]
    return result

# Selection function : create a pool of chromosomes based on their fitness
def Selection(pool):
    maxFitness = fitness_fn(population[0])
    for i in range(population_size):
        if maxFitness != 0:
            fitness = fitness_fn(population[i])/maxFitness
        else:
            fitness = 0.01
        n = int(fitness * 100)
        for _ in range(n):
            pool.append(population[i])
    return pool



letters = "ابپتثجچحخدذرزژسشصضطظعقفغکگلمنوهی0123456789؟! .،؛آ"

population_size = 200
mutation_rate = 0.03
generations = 1000

target = input()
temp = ''
population = []
# First Population (all random)
for i in range(population_size):
    for j in range(len(target)):
        temp += temp.join(random.choice(letters))
    population.append(temp)
    temp = ''

# Calculate generations
for gen in range(generations):
    population.sort(key=fitness_fn,reverse=True) # sort Population by Fitness
    
    # Check for possible answer
    if target in population:
        break
    
    # Print Each generation
    print(f"Best Design in Generation {gen} : {population[0]} , Fitness = {100*fitness_fn(population[0])/math.pow(2,len(target)):.2f}")
    
    Mating_pool = []
    Mating_pool = Selection(Mating_pool) 
    print(len(Mating_pool))
    for i in range(population_size):
        # select 2 random chromosome from pool (Fitness based)
        x = Mating_pool[random.randint(0,len(Mating_pool)-1)]
        y = Mating_pool[random.randint(0,len(Mating_pool)-1)]

        population[i] = crossover(x,y)
        
        population[i] = mutate(population[i])
    
    
    
    

population.sort(key=fitness_fn,reverse=True) 

print(f"Best Design : {population[0]} , Fitness = {100*fitness_fn(population[0])/math.pow(2,len(target)):.2f}")

