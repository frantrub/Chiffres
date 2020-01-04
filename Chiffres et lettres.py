# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 18:15:37 2019

@author: ftrub
"""


import numpy as np 
import numpy.random as random 

deck_de_cartes = np.array([1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,
                           10,10,25,50,75,100])
cartes_tirées = random.choice(deck_de_cartes, 6).tolist()
nombre_cherché = random.randint(100, 1000)

def calculs_possibles(cartes_disponibles, nombre_cherché):
    
    if nombre_cherché in cartes_disponibles:
        return "Le compte est bon !"
    
    for i in range(len(cartes_disponibles)):
        for j in range(i+1, len(cartes_disponibles)):
            x, y = cartes_disponibles[i], cartes_disponibles[j]
            x, y = max(x,y), min(x,y)
            
            nouvelles_cartes = (cartes_disponibles[:i] +
                  cartes_disponibles[i+1:j] + cartes_disponibles[j+1:])
            
            liste_des_opérateurs = [
                [x + y, "+"], [x * y, "×"], [x - y, "-"]
            ]
            if y != 0 and x % y == 0:
                liste_des_opérateurs.append([x // y, "÷"])
                
            for valeur, opérateur in liste_des_opérateurs: 
                essai = calculs_possibles(nouvelles_cartes + [valeur], 
                                          nombre_cherché)
                if essai != None: 
                    return (str(x) + " " + opérateur + " " + str(y)
                            + " = " + str(valeur) + "\n" + essai)
    return None
          
print("Nombre à trouver : " + str(nombre_cherché))
print("Cartes tirées : " + str(cartes_tirées) + "\n")
Résultat = calculs_possibles(cartes_tirées, nombre_cherché)
if Résultat == None: 
    print("Il n'existe pas de solution :'(")
else:
    print(Résultat)
                
                
                
 #Utiliser fonction récursive 
                
                
                
            
          
            