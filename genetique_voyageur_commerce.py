import random
import math


matrice_distances = [
    [0, 2, 7, 15, 2, 5, 7, 6, 5, 8],
    [2, 0, 8, 10, 4, 7, 3, 7, 15, 8],
    [7, 8, 0, 1, 4, 3, 3, 4, 2, 3],
    [15, 10, 1, 0, 2, 15, 7, 7, 5, 4],
    [2, 4, 4, 2, 0, 7, 3, 2, 2, 7],
    [5, 7, 3, 15, 7, 0, 1, 7, 2, 10],
    [7, 3, 3, 7, 3, 1, 0, 2, 1, 3],
    [6, 7, 4, 7, 2, 7, 2, 0, 1, 10],
    [5, 15, 2, 5, 2, 2, 1, 1, 0, 15],
    [8, 8, 3, 4, 7, 10, 3, 10, 15, 0]
]



def calculer_distance(solution):
    distance = 0
    for i in range(len(solution) - 1):
        distance += matrice_distances[solution[i]][solution[i + 1]]
    distance += matrice_distances[solution[-1]][solution[0]]
    return distance



def creer_population(nb_villes, taille_pop):
    population = []
    for _ in range(taille_pop):
        chemin = list(range(nb_villes))
        random.shuffle(chemin)
        population.append(chemin)
    return population




def evaluer_population(population):
    return [1 / calculer_distance(indiv) for indiv in population]


def selection_par_roulette(population, fitness):
    total = sum(fitness)
    r = random.random()
    cumul = 0
    for indiv, fit in zip(population, fitness):
        cumul += fit / total
        if r <= cumul:
            return indiv



def selection_par_rang(population, fitness):

    individus_tries = [x for _, x in sorted(zip(fitness, population))]
    n = len(individus_tries)
    somme_rangs = n * (n + 1) / 2
    cumul = 0
    r = random.random()
    for idx, indiv in enumerate(individus_tries):
        rang = idx + 1
        cumul += rang / somme_rangs
        if r <= cumul:
            return indiv


def croisement_simple_point(parent1, parent2):
    n = len(parent1)
    point = random.randint(1, n - 2)
    enfant = parent1[:point]
    for ville in parent2:
        if ville not in enfant:
            enfant.append(ville)
    return enfant



def croisement_double_point(parent1, parent2):
    n = len(parent1)
    a, b = sorted(random.sample(range(n), 2))
    enfant = [None] * n
    enfant[a:b] = parent1[a:b]
    pos = b
    for ville in parent2:
        if ville not in enfant:
            if pos >= n:
                pos = 0
            enfant[pos] = ville
            pos += 1
    return enfant



def croisement_uniforme(parent1, parent2):
    n = len(parent1)
    enfant = [-1] * n
    masque = [random.choice([0, 1]) for _ in range(n)]

    for i in range(n):
        if masque[i] == 1:
            enfant[i] = parent1[i]

    for ville in parent2:
        if ville not in enfant:
            for i in range(n):
                if enfant[i] == -1:
                    enfant[i] = ville
                    break
    return enfant



def mutation(individu, taux_mutation):
    individu = individu[:]
    if random.random() < taux_mutation:
        i, j = random.sample(range(len(individu)), 2)
        individu[i], individu[j] = individu[j], individu[i]
    return individu



def algorithme_genetique(nb_villes=10, taille_pop=30, nb_generations=200, taux_mutation=0.2, type_croisement="double"):
    population = creer_population(nb_villes, taille_pop)

    for generation in range(nb_generations):
        fitness = evaluer_population(population)
        nouvelle_pop = []

        for _ in range(taille_pop):
            parent1 = selection_par_rang(population, fitness)
            parent2 = selection_par_roulette(population, fitness)

            if type_croisement == "simple":
                enfant = croisement_simple_point(parent1, parent2)
            elif type_croisement == "uniforme":
                enfant = croisement_uniforme(parent1, parent2)
            else:
                enfant = croisement_double_point(parent1, parent2)

            enfant = mutation(enfant, taux_mutation)
            nouvelle_pop.append(enfant)

        population = nouvelle_pop


        meilleures_distances = [calculer_distance(ind) for ind in population]
        print(f"Génération {generation + 1} - Meilleure distance : {min(meilleures_distances):.2f}")

    # Résultat final
    meilleures_distances = [calculer_distance(ind) for ind in population]
    meilleur = population[meilleures_distances.index(min(meilleures_distances))]
    print("\n🔹 Meilleur chemin trouvé :", meilleur)
    print("🔹 Distance minimale :", min(meilleures_distances))



print("croissement simple point")
algorithme_genetique(type_croisement="simple")

print("croissement double point")
algorithme_genetique(type_croisement="double")
algorithme_genetique(type_croisement="double")

print("croissement uniforme")
algorithme_genetique(type_croisement="uniforme")
