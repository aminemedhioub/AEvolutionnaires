import math
import random



def calculer_distance_totale(solution, matrice_distances):
    distance_totale = 0
    for i in range(len(solution) - 1):
        distance_totale += matrice_distances[solution[i]][solution[i + 1]]
    distance_totale += matrice_distances[solution[-1]][solution[0]]
    return distance_totale


def generer_voisin(solution):
    i, j = random.sample(range(len(solution)), 2)
    voisin = solution[:]
    voisin[i], voisin[j] = voisin[j], voisin[i]
    return voisin


def recuit_simule(matrice_distances, temperature_initiale, refroidissement, iterations):
    nombre_villes = len(matrice_distances)
    solution_actuelle = list(range(nombre_villes))
    random.shuffle(solution_actuelle)
    meilleure_solution = solution_actuelle[:]
    meilleure_distance = calculer_distance_totale(solution_actuelle, matrice_distances)

    temperature = temperature_initiale

    for t in range(iterations):

        voisin = generer_voisin(solution_actuelle)
        distance_actuelle = calculer_distance_totale(solution_actuelle, matrice_distances)
        distance_voisin = calculer_distance_totale(voisin, matrice_distances)

        delta = distance_voisin - distance_actuelle

        if delta < 0 or random.random() < math.exp(-delta / temperature):
            solution_actuelle = voisin[:]
            if distance_voisin < meilleure_distance:
                meilleure_solution = voisin[:]
                meilleure_distance = distance_voisin


        temperature = refroidissement * temperature

    return meilleure_solution, meilleure_distance


matrice_distances = [
    [0, 2, 9, 10],
    [1, 0, 6, 4],
    [15, 7, 0, 8],
    [6, 3, 12, 0]
]


solution, distance = recuit_simule(
    matrice_distances,
    temperature_initiale=100,
    refroidissement=0.95,
    iterations=1000
)


print("Meilleure solution trouvée (Recuit simulé):", solution)
print("Distance minimale:", distance)
