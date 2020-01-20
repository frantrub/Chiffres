# Countdowngame

L'objectif du projet est d'écrire un algorithme en python capable de gagner au jeu des Chiffres des Chiffres et des Lettres. 
J'ai finalement réalisé trois programmes, deux programmes de résolution du jeu et un programme qui génère la musique du jeu. 

# 1. La résolution du jeu 

J'ai réalisé deux algorithmes de résolution du jeu, l'un plus rapide, l'autre plus complet. 

Le premier programme (Chiffres 1.py) s'arrête dès qu'une solution est trouvée et ne renvoie rien s'il n'existe pas de solution. 
Le second programme (Chiffres 2.py) renvoie la solution dont le nombre d'étapes est minimal, et s'il n'existe pas de solution exacte, 
renvoie le calcul qui donne le résultat le plus proche possible du nombre à trouver
(comme il est demandé dans le jeu original). 

Solution de programmation choisie: 

Je me suis proposé de résoudre chaque fois un problème aléatoire (nombre cherché et nombres à utilisés tirés au sort), mais l'on peut
facilement modifier ces programmes pour résoudre un problème particulier auquel on chercherait une solution. 
Les deux programmes utilisent une fonction récursive de back-tracking. 
Cette solution s'est imposée par son élégance et sa légéreté en termes de mémoire. 
Il eût été impossible de garder en mémoire tout les calculs effectués jusqu'à ce que le solution soit trouvée (ordre de grandeur de plusieurs dizaines de millions). 

# 2. La musique du jeu 

J'ai également réalisé un programme d'orchestre virtue l(Musique_chiffres.py), afin de simuler la musique du jeu télévisé des Chiffres et des Lettres.
J'ai crée les différents instruments et une partition afin d'en extraire en fichier wav. 

Le programme ne lance pas le fichier wav, il faut le lancer à la main, avec VLC par exemple. 

# 3. Idées d'améliorations

J'avais une expérience quasi nulle de la programmation informatique avant la réalisation de ce projet. Cela m'a pris beaucoup de temps 
de comprendre l'utilisation des différents outils, notamment l'utilisation de git. 
J'aurais aimé réunir les deux programmes (de résolution et de musique) et rajouter un affichage graphique (une image du jeu par exemple), pour qu'en lançant le programme, la musique se lance automatiquement pendant que s'affiche de manière esthétique la résolution d'un problème des Chiffres et des lettres. Mais le temps m'a manqué.
