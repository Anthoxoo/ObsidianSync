**Shell :** [ optionnel ], souligné --> obligatoire, | ou exclusif, ... plusieurs options possibles : ex fichier 1, fichier 2... Renvoie 0 si la commande passée n'a pas provoquée d'erreur, sinon le nombre renvoyé sera plus grand que 0.

**Droits :** w write, x execute, r read, u user, o other, g group

**Liens :** pour faire un lien on effectue la commande ``ln source destination`` mais meme si on supprime la source, le fichier destination restera car c'est un lien physique alors que pour un lien symbolique, c'est simplement un raccourcis donc si on détruis la source alors elle aussi ne sera plus là.

**Languages de programmation :** languages bas niveau compilés une seule fois puis utilisable tout le temps  (ou presque) comme c,go,rust... ou languages haut niveau comme python,bash... qui vont etre compilés au fur et a mesure donc on a besoin du code source a coté a chaque fois que l'on veut l'éxecuter et enfin un entre deux comme en java ou on va d'abord traduire en code simple avant de traduire en code machine avec la JVM

**Context Switch :** Le context switch permet à l'OS de conserver un processus dans un état meme en l'ayant mis en pause afin d'y revenir plus tard si un autre processus avec des plus hauts privilèges venait à arriver. On enregistre en mémoire l'état des régistres avant pour pouvoir revenir a ce meme état après, on en revient a la sécurité ou meme pendant un contxt switch, aucun programme ne peut interférer avec le programme mis en pause.

**processus :** [[Schéma processus-2]]. lorsqu'un processus est terminé, celui-ci va faire un systeme call afin de dire qu'il a terminé et que l'OS vienne récupérer les ressources précedemment allouées.

**Ordonnancement :** ordo a connaitre : shortest first, round robin, shortest remaining, fifo + voir [[CM_05_BAS.pdf]] à la fin.

