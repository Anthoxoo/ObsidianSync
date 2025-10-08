[[TD3 - BAS.pdf]]
# Exercice 4 :
```sh
#!/bin/sh


/dev/null pour envoyer a la poubelle sans afficher le résultat du grep
if ls -l "$1" | grep '^...x' > /dev/null; then
  echo "OK"
  exit 0
fi
exit 1

```

# Exercice 5 :
```sh
#!/bin/sh

if [ $# -ne 1 ];then
  echo "Usage : $0 parametre" >&2
  exit 1
fi
exit 0
```

# Exercice 6 :
```sh
#A FAIRE
```

# Exercice 7 :
```sh
#!/bin/sh


#Vérifie qu'il y a 2 parametres
if [ $# -ne 2 ]; then
  echo "Usage : $0 entier1 entier2" >&2
  exit 1
fi

test $1 -gt 0 #Vérifie que $1 est positif
if test $? -ne 0;then
  echo "$1 n'est pas strictement positif" >&2
  exit 2
fi

test $2 -gt 0 #Vérifie que $2 est positif
if test $? -ne 0;then
  echo "$2 n'est pas strictement positif" >&2
  exit 2
fi

if test $1 -gt $2;then
  echo "OK"
  exit 1
fi
```

# Exercice 8
```sh
#! /bin/sh

i=0
for param in "$@";do #$@ permet de mettre tous les param sur une seule ligne
#On peut aussi mettre for param et ca fera la meme chose car sh considère
#que sans rien après le param il va automatiquement prendre dans les params
  i=`expr $i + 1`
  echo Parametre$i = $param
done
exit 0
```