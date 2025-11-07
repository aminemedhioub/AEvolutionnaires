import random
from collections import deque

def calculer_cout(solution, durees):
    temps_total = 0
    cumul = 0
    for tache in solution:
        cumul += durees[tache]
        temps_total += cumul
    return temps_total

def generer_voisins(solution):
    voisins = []
    n = len(solution)
    for i in range(n):
        for j in range(i + 1, n):
            voisin = solution[:]
            voisin[i], voisin[j] = voisin[j], voisin[i]
            voisins.append(voisin)
    return voisins

def tabu_search(durees, nombre_iterations, taille_tabu):
    nb_taches = len(durees)
    solution_actuelle = list(range(nb_taches))
    random.shuffle(solution_actuelle)
    meilleure_solution = solution_actuelle[:]
    meilleure_valeur = calculer_cout(solution_actuelle, durees)
    tabu_list = deque(maxlen=taille_tabu)

    for _ in range(nombre_iterations):
        voisins = generer_voisins(solution_actuelle)
        voisins = [v for v in voisins if v not in tabu_list]
        if not voisins:
            break
        solution_actuelle = min(voisins, key=lambda x: calculer_cout(x, durees))
        valeur_actuelle = calculer_cout(solution_actuelle, durees)
        tabu_list.append(solution_actuelle[:])
        if valeur_actuelle < meilleure_valeur:
            meilleure_solution = solution_actuelle[:]
            meilleure_valeur = valeur_actuelle

    return meilleure_solution, meilleure_valeur

durees = [5, 8, 3, 6, 2, 4]
nombre_iterations = 500
taille_tabu = 30

meilleure_solution, meilleur_cout = tabu_search(durees, nombre_iterations, taille_tabu)

print("Ordre optimal trouvé (indices):", meilleure_solution)
print("Ordre des tâches:", ["T" + str(i+1) for i in meilleure_solution])
print("Coût total minimal:", meilleur_cout)
