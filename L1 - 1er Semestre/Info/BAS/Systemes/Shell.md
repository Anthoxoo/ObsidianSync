### Métacaracteres
- caracteres génériques permettant (voir moodle)
- Question : Comment supprimer tous les fichiers ayant un patterne similaire ex : imageXXX.jpg
	-  métacaracteres permettent de créer une liste de noms de fichiers tous espacés les uns des autres
	- * désigne une chaine de carac
	- ? un carac quelconque
	- . fichiers cachés
	- [liste carac] désigne ce qu'il y a entre les crochets : [0-9] "entre 0 et 9"
	- ex :
		- ```
 	  	  rm *.jpg
	  	  ```
		  -> supprime tous les jpg
		- ```
  	  	  rm image???.jpg
	  	  ```
		  -> supprime tous les fichiers ayant ce patterne
	- ; -> plusieurs commandes sur une meme ligne
	- "" quand caracteres spécial pour pas que le shell ne le prenne pour un métacaractere
	- ‵ « capture » la sortie standard pour former un nouveau paramètre ou une nouvelle commande
	- & suivi d’un chiffre permet de désigner les unités standard lors des redirections. & placé après une commande permet de lancer la commande en arrière plan
	- | permet de réaliser un branchement de commandes
	- $ retourne la valeur de la variable qui suit (il ne doit pas y avoir d’espace entre le métacaractère $ et le nom de la variable)

--- 
### Redirections 
^Redirections

- stdin -> entrée
- stdout -> sortie
- stderr -> erreur
- redirections permettent de changer les connexions par défaut entre unité logiques et unité physique
- soit ctrl + d soit commande << separateur
	-> ctrl + d envoie résultat dès que commande rentrée alors que << fait un script et envoie sur stdout
- < permet de faire le lien entre une commande et un fichier ex : 
	- ```
	  grep "n" < fichier.txt
	  ```
	  -> renvoie tous les mots ayant n de fichier.txt
- > prend permet de connecter une commande a un fichier ex :
	- ```
	  grep 'e' > fichier2.txt
	  ```
	  -> écris les mots ayant un e dans fichier2.txt
- >> fait pareil que > mais n'efface pas le fichier car un seul > reset tout si jamais le fichier existe déja ou le crée si il n'existe pas
- commande1|commande2 -> 2 commandes d'affilé et de connecter stout de commande1 a stdin de commande2. ex:
	- ```
	  cat fichier.txt | grep 'e' | grep '2' | wc -l
	  ```
	  -> envoie sur stdout les lignes où il y a un 2 et un e
  - backquote permet de prendre ce que ferait la commande de base et de le renvoyer sous forme de stdout ex :
	- grep 'e' backquote(ls) renvoie tous les mots où il y a un e des fichiers présents dans le répertoire actuel. marche de la meme maniere que << 
- mettre un 2 avant le > désigne la sortie des erreurs stderr
- **ATTENTION :** 
![[Pasted image 20250922075139.png]]


### Expression Régulières 
- Mettre toutes les epressions régulières voir CM_4

--- 
### Script
- Ensemble de commandes unix dans un meme fichier
- "#" pour mettre des commentaires
- extension souvent .(shell utilisé)
- lancer un script :
	- mettre le chemin d'accès du script avec .sh mais besoin de **mettre les droits d'éxécution** 
	-> pour mettre droits d'exec : chmod u+x monScript.sh
- un script est exec dans le shell courant appelé shell père
	- le shell fils est de meme nature que le shell père ( shell père bash --> shell fils bash )
	- Pour **forcer un script a se lancer sur le shell que l'on veut** il faut mettre dans la première ligne ex : # !bin/sh ( dans ce cas force le script a se lancer en sh )
- On peut récupérer les **valeurs des paramètres** à l'aide du $, $0 donne le non du fichier exécuté si pas de param alors donne chaine de carac vide
	- $# donne le nombre de param
	- $* et $@ : chaîne de caractères composée par la liste des paramètres, séparés par des espaces
		- "$\*" est remplacé par un seul mot ( sans le \ )
		- "$@" est remplacé par la liste des paramètres dans laquelle chaque paramètre est un mot différent
	- $? : code de retour de la dernière commande exécutée dans le shell
	- $x2 : numéro du processus du shell 
- Pour modifier la valeur des param on utilise "set"

- #### Variables 
- une variable **ne peut pas** commecer par un chiffre
- la valeur d'une variable est obtenue en mettant le signe $ juste avant
- il n'y a **que** des chaines de carac en shell
- pour affcter une valeur en shell on met nomVariable=valeur **attention pas d'espace entre = et les deux cotés**
- Attention '' et "" ne font pas pareil : 
	- ' ' protège les caractères dont le shell ne va pas les interpreter alors que " " le shell interprète mais fait un seul paramètre
- Pour modifier la valeur d'une valeur on utilise la commande "read"
- si on veut concatener des variables et autres il faut mettre des {nomVariable}
- Il est possible de faire :
- ```sh
var=p
	  ${var}wd
	  -> Lancement de la commande pwd  
	     ```

### Conditions :
- commande renvoie 0 --> condition est vraie
- commande renvoie != 0 --> condition fausse
- **Commande test :**
	- test comparaison1 -a comparaison2 
		--> ET logique ( and )
	- test comparaison1 -o comparaison2 
		--> OU logique ( or ) 
- if [ conditon ] faire **attention aux espaces dans les crochets** a respecter !
- après un if on met un then, après un elif on met un then, après un else non
- quand on ferme la condition finale on écrit "fi" 
- | signifie "ou"
- ;; signifie break

--- 
### Codes erreur :
- 0 --> VRAI
- 1 --> FAUX
- > 1 --> Commande stopée pour une quelconque raison

--- 
### Structures de contrôle
- **while** :
	- do après un while et done une fois la séquence de commandes écrite
- **boucle for** :
	- **for** myVariable **in** liste_de_cas
	- on met un do après et un done une fois la séquence de commande écrite
- 

[[CM_03_Shell_BAS.pdf]]
[[CM_04_Shell8BAS.pdf]]
[[TD1 BAS.pdf]]