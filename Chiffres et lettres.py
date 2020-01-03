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
    if N==1 :
        return False
    else : 
        for i in range(N-1):
            for j in range(i+1,N):
                x=cartes_restantes[i]
                y=cartes_restantes[j]
                a=x+y
                b=x*y
                c=np.abs(x-y)
                if min(x,y)!=0:
                    d=max(x,y)//min(x,y)
                    if (a==nombre_cherché or b==nombre_cherché 
                    or c==nombre_cherché or d==nombre_cherché) :
                        return True
                    else:
                        nouvelles_cartes=(cartes_restantes[:i]+cartes_restantes[i+1:j]
                        +cartes_restantes[j+1:])
                        essai=calculs_possibles(nouvelles_cartes+[a])
                        if essai : 
                            return True 
                        essai=calculs_possibles(nouvelles_cartes+[b])
                        if essai : 
                            return True
                        calculs_possibles(nouvelles_cartes+[c])
                        if essai : 
                            return True
                        if divmod(max(x,y),min(x,y))[1]==0:
                                calculs_possibles(nouvelles_cartes+[d])
                                if essai : 
                                    return True
                else:
                    if (a==nombre_cherché or b==nombre_cherché 
                    or c==nombre_cherché):
                        return True
                    else:
                        nouvelles_cartes=(cartes_restantes[:i]+cartes_restantes[i+1:j]
                        +cartes_restantes[j+1:])
                        essai = calculs_possibles(nouvelles_cartes+[a])
                        if essai : 
                            return True
                        calculs_possibles(nouvelles_cartes+[b])
                        if essai : 
                            return True
                        calculs_possibles(nouvelles_cartes+[c])
                        if essai : 
                            return True 
                        
          
            
                
                
                
 #Utiliser fonction récursive 
                
                
                
            
          
            