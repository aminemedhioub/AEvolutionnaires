import random
import math

def calculer_distance_totale(solution, matrice_distances):
    distance_totale = 0
    for i in range(len(solution) - 1):
        distance_totale += matrice_distances[solution[i]][solution[i + 1]]
    distance_totale += matrice_distances[solution[-1]][solution[0]]
    return distance_totale

def generer_voisins(solution):
    voisins = []
    for i in range(len(solution)):
        for j in range(i + 1, len(solution)):
            voisin = solution[:]
            voisin[i], voisin[j] = voisin[j], voisin[i]
            voisins.append(voisin)
    return voisins

def recuit_simule(matrice_distances, temperature_initiale, refroidissement, iterations):
    nombre_villes = len(matrice_distances)
    solution_actuelle = list(range(nombre_villes))
    random.shuffle(solution_actuelle)
    meilleure_solution = solution_actuelle[:]
    distance_actuelle = calculer_distance_totale(solution_actuelle, matrice_distances)
    meilleure_distance = distance_actuelle
    temperature = temperature_initiale

    for _ in range(iterations):
        voisins = generer_voisins(solution_actuelle)
        voisin = random.choice(voisins)
        distance_voisin = calculer_distance_totale(voisin, matrice_distances)
        delta = distance_voisin - distance_actuelle

        if delta < 0 or random.random() < math.exp(-delta / temperature):
            solution_actuelle = voisin[:]
            distance_actuelle = distance_voisin

        if distance_actuelle < meilleure_distance:
            meilleure_solution = solution_actuelle[:]
            meilleure_distance = distance_actuelle

        temperature *= refroidissement

    return meilleure_solution, meilleure_distance

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

temperature_initiale = 1000
refroidissement = 0.95
iterations = 1000

solution, distance = recuit_simule(matrice_distances, temperature_initiale, refroidissement, iterations)

print("Meilleure solution trouvée :", solution)
print("Distance minimale :", distance)
