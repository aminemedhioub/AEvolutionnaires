import random



durees_taches = [5, 2, 8, 3, 6, 4, 7, 2, 9, 5]


def calculer_temps_total(ordre):
    temps_cumule = 0
    temps_total = 0
    for tache in ordre:
        temps_cumule += durees_taches[tache]
        temps_total += temps_cumule
    return temps_total


def creer_population(nb_taches, taille_pop):
    population = []
    for _ in range(taille_pop):
        ordre = list(range(nb_taches))
        random.shuffle(ordre)
        population.append(ordre)
    return population


def evaluer_population(population):
    return [1 / calculer_temps_total(indiv) for indiv in population]



def selection_par_roulette(population, fitness):
    total = sum(fitness)
    r = random.random()
    cumul = 0
    for indiv, fit in zip(population, fitness):
        cumul += fit / total
        if r <= cumul:
            return indiv


def selection_par_rang(population, fitness):
    individus_tries = [x for _, x in sorted(zip(fitness, population), reverse=True)]
    n = len(individus_tries)
    somme_rangs = n * (n + 1) / 2
    cumul = 0
    r = random.random()
    for rang, indiv in enumerate(individus_tries, start=1):
        cumul += rang / somme_rangs
        if r <= cumul:
            return indiv



def croisement_simple_point(parent1, parent2):
    n = len(parent1)
    point = random.randint(1, n - 2)
    enfant = parent1[:point]
    for t in parent2:
        if t not in enfant:
            enfant.append(t)
    return enfant



def croisement_double_point(parent1, parent2):
    n = len(parent1)
    a, b = sorted(random.sample(range(n), 2))
    enfant = [None] * n
    enfant[a:b] = parent1[a:b]
    pos = b
    for t in parent2:
        if t not in enfant:
            if pos >= n:
                pos = 0
            enfant[pos] = t
            pos += 1
    return enfant



def croisement_uniforme(parent1, parent2):
    n = len(parent1)
    enfant = [-1] * n
    masque = [random.choice([0, 1]) for _ in range(n)]
    for i in range(n):
        if masque[i] == 1:
            enfant[i] = parent1[i]
    for t in parent2:
        if t not in enfant:
            for i in range(n):
                if enfant[i] == -1:
                    enfant[i] = t
                    break
    return enfant



def mutation(individu, taux_mutation):
    individu = individu[:]
    if random.random() < taux_mutation:
        i, j = random.sample(range(len(individu)), 2)
        individu[i], individu[j] = individu[j], individu[i]
    return individu



def algorithme_genetique(nb_taches=10, taille_pop=30, nb_generations=200, taux_mutation=0.2, type_croisement="double"):
    population = creer_population(nb_taches, taille_pop)

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

        meilleurs_temps = [calculer_temps_total(ind) for ind in population]
        print(f"Génération {generation+1} - Meilleur temps total : {min(meilleurs_temps)}")

    meilleurs_temps = [calculer_temps_total(ind) for ind in population]
    meilleur = population[meilleurs_temps.index(min(meilleurs_temps))]
    print("Meilleur ordre de tâches :", meilleur)
    print("Temps total minimal :", min(meilleurs_temps))




print("croissement simple point:")
algorithme_genetique(type_croisement="simple")

print("croissement double point:")
algorithme_genetique(type_croisement="double")

print("croissement uniforme")
algorithme_genetique(type_croisement="uniforme")
