# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 19:01:41 2020

@author: ftrub
"""

import numpy as np
import numpy.random as random


def calculs_possibles(cartes_disponibles, nombre_cherché):

    valeur_min, calcul_min, etapes_min = 0, "", np.infty
    
    for x in cartes_disponibles:
        if abs(x-nombre_cherché) < abs(valeur_min-nombre_cherché):
            valeur_min = x
            calcul_min = str(x) + " est la solution la plus proche."
            etapes_min = 0
    
    for i in range(len(cartes_disponibles)):
        for j in range(i+1, len(cartes_disponibles)):
            x, y = cartes_disponibles[i], cartes_disponibles[j]
            x, y = max(x, y), min(x, y)

            nouvelles_cartes = (cartes_disponibles[:i] +
                                cartes_disponibles[i+1:j] +
                                cartes_disponibles[j+1:])

            liste_des_opérateurs = [
                [x + y, "+"], [x * y, "×"], [x - y, "-"]
            ]
            if y != 0 and x % y == 0:
                liste_des_opérateurs.append([x // y, "÷"])

            for valeur, opérateur in liste_des_opérateurs:
                essai = calculs_possibles(nouvelles_cartes + [valeur],
                                          nombre_cherché)
                if (
                    (abs(essai[0]-nombre_cherché) <
                        abs(valeur_min-nombre_cherché)) or
                    ((abs(essai[0]-nombre_cherché) ==
                        abs(valeur_min-nombre_cherché)) and
                     essai[2]<etapes_min)):
                    valeur_min = essai[0]
                    calcul_min = (str(x) + " " + opérateur + " " + str(y) +
                                  " = " + str(valeur) + "\n" + essai[1])
                    etapes_min = essai[2] + 1
                    
    return [valeur_min, calcul_min, etapes_min]


if __name__ == "__main__":
    deck_de_cartes = np.array([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8,
                               9, 9, 10, 10, 25, 50, 75, 100])
    cartes_tirées = random.choice(deck_de_cartes, 6, replace = False).tolist()
    nombre_cherché = random.randint(100, 1000)

    print("Nombre à trouver : " + str(nombre_cherché))
    print("Cartes tirées : " + str(cartes_tirées) + "\n")
    valeur, résultat, étapes = calculs_possibles(cartes_tirées, nombre_cherché)
    print("Le résultat le plus proche est " + str(valeur))
    print("Voici le calcul associé (en un nombre minimal d'étapes) :\n" +
          résultat)
