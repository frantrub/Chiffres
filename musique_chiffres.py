# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 11:59:00 2019

@author: ftrub

Ce programme renvoie un fichier wav de la musique des Chiffres et des Lettres. 

Il effectue pour cela trois choses : 
    -Il crée des instruments
    -Il crée une partition
    -Il transforme les fonctions générées en fichier son

"""

import numpy as np 
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
from numpy.random import random 

#Création et affichage de fonctions de signal sonore classiques 
#(sinusoïdale, triangulaire, en dents de scie, en créneaux) 
#afin d'obtenir différents timbres pour les instruments. 

def sine_wave(t,f) : 
    """valeur ton pur 
    de fréquence f en hertz en fonction du temps t en seconde"""
    return(np.sin(2*np.pi*t*f))
 
x=[i/299 for i in range(300)]
y=[sine_wave(i,4) for i in x]
plt.plot(x,y)    

def square_wave(t,f):
    """valeur onde en créneaux 
    de fréquence f en herts en fonction du temps t en seconde"""
    return(1.0-2*((int(t*2*f))%2))

x=[i/299 for i in range(300)]
y=[square_wave(i,4) for i in x]
plt.plot(x,y)    

def sawtooth_wave (t,f):
    """valeur onde en dents de scie 
    de fréquence f en herts en fonction du temps t en seconde"""
    return(-1+((t*2*f)%2))

x=[i/299 for i in range(300)]
y=[sawtooth_wave(i,4) for i in x]
plt.plot(x,y)  

def triangle_wave(t,f):
   """valeur onde en triangle 
   de fréquence f en herts en fonction du temps t en seconde"""
   return abs(((f*t)%1.0)-1/2)*4-1

x=[i/299 for i in range(300)]
y=[triangle_wave(i,4) for i in x]
plt.plot(x,y) 

sample_rate=44100 #nombre d'échantillons par seconde
la440=440

#Création d'un outil de création de partitions

def frequence_note(nb_demis_tons): 
    """renvoie la fréquence en hertz 
    en fonction de la distance en demis-tons du la440"""
    return la440*2**(nb_demis_tons/12)

#partition test de Frère_Jacques, en deux voix (canon)

frere_jacques = [(0,1),(2,1),(4,1),(0,0.9),(None,0.1),(0,1),(2,1),(4,1),(0,0.9),
                 (None,0.1),(4,1),(5,1),(7,1.9),(None,0.1),(4,1),(5,1),(7,1.9),(None,0.1),
                 (7,0.75),(9,0.25),(7,0.5),(5,0.5),(4,1),(0,0.9),(None,0.1),
                 (7,0.75),(9,0.25),(7,0.5),(5,0.5),(4,1),(0,0.9),(None,0.1),
                 (0,1),(-5,1),(0,1),(None,1),(0,1),(-5,1),(0,1),(None,9)]

frere_jacques2 = [(None,8),(0,1),(2,1),(4,1),(0,0.9),(None,0.1),(0,1),(2,1),(4,1),(0,0.9),
                 (None,0.1),(4,1),(5,1),(7,1.9),(None,0.1),(4,1),(5,1),(7,1.9),(None,0.1),
                 (7,0.75),(9,0.25),(7,0.5),(5,0.5),(4,1),(0,0.9),(None,0.1),
                 (7,0.75),(9,0.25),(7,0.5),(5,0.5),(4,1),(0,0.9),(None,0.1),
                 (0,1),(-5,1),(0,1),(None,1),(0,1),(-5,1),(0,1.5)]

#Différentes fonctions permettant de créer une partition et de l'exporter en wav.

def jouer_note(nb_demis_tons,duree,forme_d_onde):
    """INT crée une onde échantillonnée 
    nb_demis_tons : écarts au la 440 en demis-tons
    durée : en noires"""
    if nb_demis_tons == None : #gestion des silences
        return [0 for i in range (int(sample_rate*duree))]
    else: 
        return [forme_d_onde(i/sample_rate,frequence_note(nb_demis_tons))
            for i in range (int(sample_rate*duree))]
    
    
def partition(notes,forme_d_onde,tempo):
    """échantillonne une suite de notes
    notes : liste de tuples (couples) demis-tons du la, duree 
    forme d'onde : fonction d'onde choisie
    tempo: duree de la noire"""
    data=[]
    for nb_demis_tons,duree in notes : 
        data+=jouer_note(nb_demis_tons,duree*(60/tempo),forme_d_onde)
    return data
    
def export_partition(data,nom) : 
    """Exporte une suite de notes en fichier wave
    Le sample_rate correspond au nombre de points mis dans une même seconde
    On passe data en array (considéré par la scipy.wave.write)"""
    return wav.write(nom+'.wav',sample_rate,np.array(data))


def mix (*data): 
    """Moyenne de plusieurs partitions, 
    rend comme la simultanéité du jeu de ces partitions"""
    return [(sum(d))/len(data) for d in zip(*data)]

def gain (data,gain):
    """Permet de gérer les volumes relatifs des différentes partitions"""
    return [i*gain for i in data]


#Fonctions d'effets permettant de créer des instruments plus sophistiqués: 

def reduction_rapide (fonction_d_onde,alpha=5):
    """Permet de créer des instruments au timbre percusif"""
    def nouvelle_fonction (t,f):
        return fonction_d_onde(t,f)*np.exp(-alpha*t)
    return nouvelle_fonction

def bruit_blanc(t,f):
    return random()*2-1

#Instruments à effets : 

glokenspiel = reduction_rapide(triangle_wave) #Glokenspiel est une fonction qui dépend de t et f
glokenspiel2=reduction_rapide(triangle_wave,8)

Charleston = reduction_rapide(bruit_blanc,20)

#Fonction finale 

def conducteur (infos_partitions,tempo,nom):
    x=[]
    for notes, volume, onde in infos_partitions :
        x.append(gain(partition(notes,onde,tempo),volume))
    return export_partition(mix(*x),nom)

#Différentes voix de la musique des Chiffres:

musique_chiffres= [(7,1),(14,1),(7,1),(14,1),(7,1),(14,1),(7,1),(14,1),(7,1),(14,1),(7,1),(14,1),
                   (12,1/3),(14,1/3),(17,1/3),(19,1/3),(21,1/3),(24,1/3),(26,1)]
basse_chiffres1= [(-5,12),(None,3)]
basse_chiffres2=[(-5.05,12),(None,3)]
basse_chiffres3=[(-4.95,12),(None,3)]
contre_temps_chiffres=[(None,0.5),(None,1),(None,1),(None,1),(None,1),(None,1),(None,1),(None,1),
                       (19,1),(19,1),(19,1),(19,1),(19,1),(None,2.5)]
batterie_chiffres=[(7,1/2),(14,1/2),(7,1/2),(14,1/2),(7,1/2),(14,1/2),
                   (7,1/2),(7,1/2),(14,1/2),(7,1/2),
                   (14,1/2),(7,1/2),(14,1/2),(7,1/2),(7,1/2),
                   (7,1/2),(14,1/2),(7,1/2),(14,1/2),(7,1/2),(14,1/2),
                   (7,1/2),(7,1/2),(14,1/2),(None,3)]

#Partition complète des Chiffres

infos_partitions=[(musique_chiffres,1,glokenspiel),(basse_chiffres1,1/3,sine_wave),
                  (basse_chiffres2,1/3,sine_wave),(basse_chiffres3,1/3,sine_wave),
                  (contre_temps_chiffres,0.5,glokenspiel2),(batterie_chiffres,0.3,Charleston)]
tempo=100

if __name__ == "__main__":
    conducteur(infos_partitions, tempo, 'partition_complète_chiffres')





