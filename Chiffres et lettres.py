# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 18:15:37 2019

@author: ftrub
"""


import numpy as np 
import numpy.random as random 

deck_de_cartes = np.array([1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,
                           10,10,25,25,50,50,75,75,100,100])
cartes_tirées = random.choice(deck_de_cartes, 4).tolist()
nombre_cherché = random.randint(100, 1000)

def calculs_possibles(cartes_restantes, nombre_cherché):
    if nombre_cherché in cartes_restantes:
        return "Le compte est bon !"
    for i, x in enumerate(cartes_restantes):
        for j, y in enumerate(cartes_restantes[i+1:], i+1):
            nouvelles_cartes = (cartes_restantes[:i] +
                  cartes_restantes[i+1:j] + cartes_restantes[j+1:])
            
            x, y = max(x,y), min(x,y)
            
            #Cas de l'addition :
            essai = calculs_possibles(nouvelles_cartes + [x + y],
                                 nombre_cherché)
            if essai != None:
                return str(x) + " + " + str(y) + " = " + str(x + y) + "\n" + essai
            #Cas de la multiplication :
            essai = calculs_possibles(nouvelles_cartes + [x * y],
                                 nombre_cherché)
            if essai != None:
                return str(x) + " × " + str(y) + " = " + str(x * y) + "\n" + essai
            #Cas de la soustraction :
            essai = calculs_possibles(nouvelles_cartes + [x - y],
                                 nombre_cherché)
            if essai != None:
                return str(x) + " - " + str(y) + " = " + str(x - y) + "\n"  + essai
            #Cas de la division :
            if y != 0 and x % y == 0:
                essai = calculs_possibles(
                            nouvelles_cartes + [x // y],
                            nombre_cherché)
                if essai != None: 
                    return str(x) + " ÷ " + str(y) + " = " + str(x // y) + "\n" + essai
    return None
          
print("Nombre à trouver : " + str(nombre_cherché))
print("Cartes tirées : " + str(cartes_tirées) + "\n")
Résultat = calculs_possibles(cartes_tirées, nombre_cherché)
if Résultat == None: 
    print("Il n'existe pas de solution :'(")
else:
    print(Résultat)
                
                
                
 #Utiliser fonction récursive 
                
                
                
            
          
            