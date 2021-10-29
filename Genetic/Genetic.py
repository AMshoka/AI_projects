import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


def expr(x, y):
    return -0.0001 * (
                (np.abs(np.sin(x) * np.sin(y) * np.exp(np.abs(100 - (np.sqrt(x ** 2 + y ** 2) / np.pi)))) + 1) ** 0.1)


def cal_pop_fitness(pop):
    fitness = expr(pop[:, 0], pop[:, 1])
    return fitness


def select_mating_pool(pop, fitness, num_parents):
    parents = np.empty((num_parents, pop.shape[1]))
    for parent_num in range(num_parents):
        max_fitness_idx = np.where(fitness == np.min(fitness))
        max_fitness_idx = max_fitness_idx[0][0]
        parents[parent_num, :] = pop[max_fitness_idx, :]
        fitness[max_fitness_idx] = 99999999999
    return parents


def crossover(parents, offspring_size):
    offspring = np.empty(offspring_size)

    crossover_point = np.uint8(offspring_size[1] / 2)

    for k in range(offspring_size[0]):
        parent1_idx = k % parents.shape[0]

        parent2_idx = (k + 1) % parents.shape[0]

        offspring[k, 0:crossover_point] = parents[parent1_idx, 0:crossover_point]

        offspring[k, crossover_point:] = parents[parent2_idx, crossover_point:]
    return offspring


def mutation(offspring_crossover):
    for idx in range(offspring_crossover.shape[0]):
        random_value = np.random.uniform(-1.0, 1.0, 1)
        offspring_crossover[idx, 1] = offspring_crossover[idx, 1] + random_value
    return offspring_crossover


equation_inputs = [4, -2]
num_weights = len(equation_inputs)
sol_per_pop = 8
num_parents_mating = 4
pop_size = (sol_per_pop, num_weights)
new_population = np.random.uniform(low=-4.0, high=4.0, size=pop_size)
print(new_population)

Bestresult = []
numgene = 100

for i in range(numgene):
    print("Generation : ", i)

    fit = cal_pop_fitness(new_population)
    # print("Fitness")
    # print(fit)
    Bestresult.append(np.min(expr(new_population[:, 0], new_population[:, 1])))

    print("best resul", np.min(expr(new_population[:, 0], new_population[:, 1])))

    parents = select_mating_pool(new_population, fit, num_parents_mating)
    print("Parents")
    print(parents)

    offspring_crossover = crossover(parents, offspring_size=(pop_size[0] - parents.shape[0], num_weights))
    print("Crossover")
    print(offspring_crossover)

    offspring_mutation = mutation(offspring_crossover)
    print("Mutation")
    print(offspring_mutation)
    new_population[0:parents.shape[0], :] = parents
    new_population[parents.shape[0]:, :] = offspring_mutation

fit = cal_pop_fitness(new_population)

best_match_idx = np.where(fit == np.min(fit))

print("Best solution : ", new_population[best_match_idx, :])
print("Best solution fitness : ", fit[best_match_idx])

import matplotlib.pyplot

matplotlib.pyplot.plot(Bestresult)
matplotlib.pyplot.xlabel("Iteration")
matplotlib.pyplot.ylabel("Fitness")
matplotlib.pyplot.show()
