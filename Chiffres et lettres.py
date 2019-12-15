# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 18:15:37 2019

@author: ftrub
"""


import numpy as np 
import numpy.random as random 

deck_de_cartes=np.array([1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,
                         10,10,25,25,50,50,75,75,100,100])
cartes_tirées=random.choice(deck_de_cartes,6).tolist()
nombre_cherché=random.randint(100,1000)

def calculs_possibles(cartes_restantes):
    N=len(cartes_restantes)
    for i in range(N-1):
        for j in range(i,N):
            a=cartes_restantes[i]+cartes_restantes[j]
            b=cartes_restantes[i]*cartes_restantes[j]
            c=np.abs(cartes_restantes[i]-cartes_restantes[j])
            d=(max(cartes_restantes[i],cartes_restantes[j])/
               min(cartes_restantes[i],cartes_restantes[j]))
            if a==nombre_cherché or b==nombre_cherché or c==nombre_cherché or d==nombre_cherché:
                print('solution trouvée')
            else:
                nouvelles_cartes=[k 
                              for k in cartes_restantes[:i]+cartes_restantes[j:]]
                calculs_possibles(nouvelles_cartes+[a])
                calculs_possibles(nouvelles_cartes+[b])
                calculs_possibles(nouvelles_cartes+[c])
                if d==int(d):
                    calculs_possibles(nouvelles_cartes+[d])
            
            
                
                
 #Utiliser fonction récursive 
                
                
                
            
          
            