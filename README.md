# Countdowngame

L'objectif du projet était d'écrire un algorithme en python capable de gagner à la partie Chiffres des Chiffres et des Lettres. 
J'ai finaleùent réalisé trois programmes, deux programmes de résolution du jeu et un programme qui génère la musique du jeu télévisé. 

1. La résolution du jeu 

J'ai réalisé deux algorithmes différents, l'un plus rapide, l'autre plus complet. 
Les deux programmes utilisent une fonction récursive de back-tracking. 
Le premier programme s'arrête dès qu'une solution est trouvée et ne renvoie rien s'il n'existe pas de solution. 
Le second programme renvoie la solution dont le nombre d'étapes est minimal, et s'il n'existe pas de solution exacte, 
renvoie le calcul qui donner le résultat le plus proche possible du nombre à trouver
(comme il est demandé dans le jeu original). 

2. La musique 

J'ai également réalisé un programme d'orchestre virtuel, afin de simuler à partir des foncitons 
des banques 
numpy, scipy.io.wavfile, numpy.random et matplotlib.pyplot la musique du jeu télévisé des Chiffres et des Lettres.
J'ai crée différents instruments et une partition afin d'en extraire en fichier wav.
