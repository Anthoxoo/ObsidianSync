# UAL 
utilise des aditionneurs en chaines
![[Pasted image 20251201075102.png]]
**en sortie :**
8 Bits "s" qui donnent le résultat de l'opération de a op b
Bit C qui dit si l'on a une retenue
Bit Z dit si le résultat = 0
**en entrée pour op :**
00 signifie +
01 signifie -
10 signifie et
11 signifie transfert opérande à 2
![[Pasted image 20251201075257.png]]
Pour faire une UAL, on a besoin de pouvoir retenir le résultat de calculs lorsqu'on fait par exemple 1+2+3 donc on fait le calcul et on le met dans une bascule D avec un multiplexeur pour retenir le résultat.

Le processeur possède un registre PC ( program counter ) qui donne qui permet de donner les prochaines instructions à l'UE car il sait quel programme doit se lancer après.
Pour passer à l'instruction suivante il faut ajouter 2 au PC. Pour se faire on va mettre a disposition un additionneur réservé au PC qui va faire +2 à la sortie de PC.

Pour chaque variable on a besoin d'**un registre correspondant**
Lorsque l'on veut ajouter faire des oppérations avec deux variables dedans, il faut que dans "l'en-tete" de l'opération, mettre un 1 au début de celui-ci et on les branche ensemble pour ajouter le registre et la valeur voulue, si c'est une constante, on met un 0 en en-tete 

Pour coder un nombre négatif, il faut faire un déplacement donc faire une addition du nombre en question avec son inverse.

**Comment faire pour faire des boucles qui s'arretent ?**
il faut vérifier a chaque fin d'itération si on veut repartir dans la boucle ( goto ) ou alors poursuivre le code dans le programme, on peut réutiliser les sorties Z et C ( Z pour si la condition à a voir avec 0 ). Il faut donc garder en mémoire C et Z afin de pouvoir les avoir dans l'instruction suivante qui va déterminer si jamais on reste dans la boucle ou pas.