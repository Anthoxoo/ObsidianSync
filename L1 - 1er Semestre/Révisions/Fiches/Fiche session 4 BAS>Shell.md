**Shell :** pour renvoyer vers la sortie standart des erreurs il faut faire 2>fichier, après un < << > >> il faut toujours qu'il y ait un fichier derrière.

**Reggex :** Pour une répetition de n fois un caractère, tu fais `x\{5\}` pour une répétition de 5 fois le caractère x. Toujours utiliser '' quand on utilise des regex pour éviter les métacaractères 

**Script :** shbang --> #!/bin/sh. $# nombre de param, $? code renvoyé par la dernière commande, $* donne dans une seule chaine de caractère tous les paramètres
commande test : `test comparaison1 -a comparaison2` --> ET
`test comparaison1 -o comparaison2` --> OU
avec test on utilise pas de [  ] et on utilise pas != = ...
mais avec if oui et pas oublie fi a la fin.

**Commande en plus mais importantes :**
cut
- -f avec la position juste après enleve le bloc a la position donnée exemple cut -f1
- -d 'delimiteur' permet de spécifier ou on veut l'enlever exemple : `cut -d ' ' -f1` --> le premier bloc qui aura pour délimiteur un espace.
- -c suivi de pos1-pos2 ou just pos1 enleve a chaque ligne le caractere a cette position
tr 
- -s supprime un doublon exemple : `tr -s ' '` enleve tous les espaces en trop
sed
- **on utilisera toujours -e 's/....'** s pour substitution par exemple : `sed -e 's/abc/cba'`--> remplace abc par cba mais une seule fois dans la ligne, si on veut sur toute la ligne il faut le /g a la fin pour global : `sed -e 's/abc/cba/g'` on peut aussi echanger des blocs entre eux
df
- -k donne le nombre d'octet d'un fichier ou d'un répertoire.