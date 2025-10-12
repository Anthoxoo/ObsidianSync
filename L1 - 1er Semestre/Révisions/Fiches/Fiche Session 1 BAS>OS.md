**Def OS :** Un systeme d'exploitation est ce qui relie l'utilisateur au matériel de la machine, il agit comme une interface et offre a l'utilisateur une machine virtuelle afin que celui-ci puisse utiliser son ordinateur.

**Types OS :** Mono-utilisateur mono tache, multi utilisateur mono taches, multi utilisateur multi taches --> utilisé par la quasi majorité des OS désormais

**Fonctionnement Evenements :** le systeme d'exploitation attend constamment un evenement, dès qu'il en a un, il va le traiter.
Les cpus peuvent désormais gérer les evenements asynchrones --> OS va ordonner au cpu d'interrompre ce qu'il faisait actuellement et de le laisser de coté, pour exécuter le processus que l'OS va lui donner puis reprendre après le code précedemment interrompu.
Le cpu possède deux modes : le mode user qui est le mode par défaut et qui empeche a l'utilisateur d'effectuer des taches demandant des permissions élevées et le mode kernel qui permet d'effectuer ces taches demandant des permissions mais il faut faire attentions car dans ce mode, l'utilisateur peut tout faire.
Un evenement peut tout aussi bien etre un nouveau processus à effectuer comme une erreur dans un code comme une division par zero etc ce qui va provoquer l'interruption du processus actuel.

**Horloges :** la principale utilité de l'horloge de l'OS est d'éviter les boucles infinies car l'horloge va lancer un timer avec un temps x et toutes les x secondes, l'OS va vérifier si une boucle infinie ou autre erreur a été rencontrée dans le code. ou meme si le processus prend trop de ressources, l'OS prendra dans ces cas là la main et renverra une erreur a l'utilisateur.

**Comportement OS :** lors du démarrage, le bios est contenu dans la mémoire ROM se lit dès le lancement de la machine, le bios va chercher l'emplacement du bootloader afin que celui-ci donne l'emplacement de l'OS afin que celui-ci puisse charger en mémoire le kernel et booter afin que l'utilisateur puisse utiliser sa machine.