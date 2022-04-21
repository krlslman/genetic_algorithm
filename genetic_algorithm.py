import random

def cross_over(parent_A, parent_B):
    split_length  = int(random.random() * int(len(parent_A) - 1))
    child = substring(parent_A, 0, split_length ) + substring(parent_B, split_length , len(parent_B))
    
    return child

def fitness(individual):
    count_ones = 0
    for i in range(0, len(individual) - 1 + 1, 1):
        if individual[i] == "1":
            count_ones += 1
    fitness = float(countOfOnes) / len(individual)
    
    return fitness

def mutate(individual):
    if int(random.random() * 2) == 0:
        pass
    else:
        change_index = int(random.random() * len(individual))
        if individual[change_index] == "0":
            changed_character = "1"
        else:
            changed_character = "0"
        individual = substring(individual, 0, change_index) + changed_character + substring(individual, change_index + 1, len(individual))
    
    return individual

def print_array(array):
    return_string = ""
    for i in range(0, len(array) - 1 + 1, 1):
        return_string = return_string + array[i] + "    "
    
    return return_string

def substring(s, start, end):
    substring = ""
    if start < len(s):
        if end > len(s):
            end = len(s)
        for index in range(start, end - 1 + 1, 1):
            substring = substring + s[index]
    
    return substring

# Main
population = [""] * (4)

population[0] = "00000000"
population[1] = "00000010"
population[2] = "00001000"
population[3] = "00100001"
generation = 0
maximumFitnessReached = False
while not maximumFitnessReached:
    print(str(generation) + "    " + print_array(population))
    bestFitness = 0
    bestIndex = 0
    second_best_index = 0
    for i in range(0, len(population) - 1 + 1, 1):
        currentFitness = fitness(population[i])
        if currentFitness == 1.0:
            maximumFitnessReached = True
        else:
            if currentFitness >= bestFitness:
                bestFitness = currentFitness
                second_best_index = bestIndex
                bestIndex = i
    for i in range(0, len(population) - 1 + 1, 1):
        population[i] = mutate(cross_over(population[bestIndex], population[second_best_index]))
    generation = generation + 1
