
# Exercice 1
C'est entre 0 et 3000 car l'OS reprend la main puis entre 8000 et 12000 lorsque le processus p2 a été élu.

# Exercice 2
FIFO : P1 --> P2 --> P3
SFJ : P2 --> P1 --> P3
LIFO : P3 --> P2 --> P1
Random : peu importe,par exemple : p1,p3,p2

# Exercice 3
Attention, si un processus s'arrete, l'entrée sortie n'est pas affectée alors que si c'est une E/S oui
non préamptif = on ne peut pas l'arreter sauf lorsqu'il y a une inetrruption.
avec préamption = au bout d'un quantum de temps, on va forcément arreter le programme.

# Exercice 4

Attention quantum est différent pour chaque processus et ne se rénitialise pas tant qu'il n'a pas été atteint.

**CC4 : questions cours, commandes, scripts et ordonnancement.** PENSER a prendre du blanco pour le CC
Quand un processus arrive on le marque dès le début pour ne pas l'oublier et pas oublier que SE prend une UT mais direct en dessous.
