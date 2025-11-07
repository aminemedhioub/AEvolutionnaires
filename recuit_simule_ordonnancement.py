import random
import math


durees_taches = [5, 2, 8, 3, 6, 4, 7, 2, 9, 5]


def calculer_temps_total(solution):
    temps_cumule = 0
    temps_total = 0
    for tache in solution:
        temps_cumule += durees_taches[tache]
        temps_total += temps_cumule
    return temps_total

def generer_voisins(solution):
    voisins = []
    for i in range(len(solution)):
        for j in range(i + 1, len(solution)):
            voisin = solution[:]
            voisin[i], voisin[j] = voisin[j], voisin[i]
            voisins.append(voisin)
    return voisins

def recuit_simule_ordonnancement(durees, temperature_initiale, refroidissement, iterations):
    nb_taches = len(durees)
    solution_actuelle = list(range(nb_taches))
    random.shuffle(solution_actuelle)

    meilleure_solution = solution_actuelle[:]
    cout_actuel = calculer_temps_total(solution_actuelle)
    meilleur_cout = cout_actuel
    temperature = temperature_initiale

    for _ in range(iterations):
        voisins = generer_voisins(solution_actuelle)
        voisin = random.choice(voisins)
        cout_voisin = calculer_temps_total(voisin)
        delta = cout_voisin - cout_actuel

        if delta < 0 or random.random() < math.exp(-delta / temperature):
            solution_actuelle = voisin[:]
            cout_actuel = cout_voisin

        if cout_actuel < meilleur_cout:
            meilleure_solution = solution_actuelle[:]
            meilleur_cout = cout_actuel

        temperature *= refroidissement

    return meilleure_solution, meilleur_cout



temperature_initiale = 1000
refroidissement = 0.95
iterations = 1000

solution, cout = recuit_simule_ordonnancement(durees_taches, temperature_initiale, refroidissement, iterations)

print("Meilleur ordre de tâches trouvé :", solution)
print("Temps total minimal :", cout)
