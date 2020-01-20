# Countdowngame

L'objectif du projet est d'écrire un algorithme en python capable de gagner à la partie Chiffres des Chiffres et des Lettres. 
J'ai finalement réalisé trois programmes, deux programmes de résolution du jeu et un programme qui génère la musique du jeu télévisé. 

# 1. La résolution du jeu 

J'ai réalisé deux algorithmes de résolution du jeu, l'un plus rapide, l'autre plus complet. 
Les deux programmes utilisent une fonction récursive de back-tracking. 
Le premier programme (Chiffres 1.py) s'arrête dès qu'une solution est trouvée et ne renvoie rien s'il n'existe pas de solution. 
Le second programme (Chiffres 2.py) renvoie la solution dont le nombre d'étapes est minimal, et s'il n'existe pas de solution exacte, 
renvoie le calcul qui donne le résultat le plus proche possible du nombre à trouver
(comme il est demandé dans le jeu original). 

# 2. La musique du jeu 

J'ai également réalisé un programme (Musique_chiffres.py) d'orchestre virtuel, afin de simuler la musique du jeu télévisé des Chiffres et des Lettres.
J'ai crée les différents instruments et une partition afin d'en extraire en fichier wav. 

# 3. Idées d'amélioration

Si j'avais eu le temps, j'aurais réuni les deux programmes de résolution et de musique et rajouté un affichage graphique (une image du jeu), pour qu'en lançant le programme, on ait à la fois la musique et la résolution d'un problème (affichée sur l'image).
