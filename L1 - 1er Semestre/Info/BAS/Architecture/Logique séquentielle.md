Tous les compsants de la logique séquentielle possèdent une fonction de mémorisation
**Stable** : Signifie que l'on sait à l'avance l'état des sorties en fonction des entrées

### Asynchrone :
**bistable :**
- ..
**Bascule RS asynchrone :**
- deux NOR reliés entre eux
- possède exactement la meme fonction qu'un NOR classique 
- interdiction de mettre R et S à 1 en meme temps car cela rend la bascule non stable car on n'est pas capable de prédire l'état des sorties

### Temps :
**instant t^n** --> changement des entrées
**instant t^(n+1)** --> moment où les valeurs de sortie changent
Lorsque l'on fait un tableau de kernau, le résultat de celui-ci va etre nommé x^(n+1)
### Systemes Synchrone
**Synchrone** : Un circuit est synchrone si ses entrées ne sont  prises en compte qu'à un certain moment, on ajoute une entrée C qui va etre la base du circuit, ex : on prend les sorties en compte lorsque C passe de 0 à 1 ou de 1 à 0 ou lorsque C est à 1
Le signal C est souvent une horloge à signal périodique
**Bascule RS synchrone :**
- Dans le cas de l'exemple avec l'horloge, on prend en compte les entrées lorsque C passe à 1 (c'est la plupart du temps le cas.)
**Bascule D :**
- Equation : Q^(n+1) = D^(n)
**Bascule à déclenchement sur front :**
- Il y a une bascule maitre et une bascule esclave
- Une seule bascule ne peut s'activer a la fois, c'est pourquoi on partage le C des deux bascules mais on fait passer un NOT C à la bascule esclave

### Registres
Une bascule mémorise 1 bit, un registre permet donc de stocker plusieurs bits en empilant des bascules.
On peut utliser un multiplexeur suivi d'une bascule D afin de stocker un bit durant indéfini (tant que le signal n'a pas été rappelé)
P