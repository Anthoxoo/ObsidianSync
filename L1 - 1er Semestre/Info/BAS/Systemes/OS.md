Definition **systeme d'exploitation** : Logiciel permettant de faciliter l'utilisation d'un ordinateur et propose à l'utilisateur un ensemble de services.  Il fournit a chaque utilisateur une machine virtuelle qui simplifie l'architecture matérielle.

--- 
### ordre :
[[schéma ordre os.canvas|schéma ordre os]]
### Types :
- mono-utilisateur : 1 programme a la fois, existe plus trop
- mono utilisateur multitaches 
- multi utilisateur multitaches : le plus commun

--- 
### Histoire : 
^Histoire

- **1ers prototypes** : ~1945 forcément tres primitifs.
- **2eme gen** :~1950 cpu ( central process unit ) permettant de faire plusieurs choses a la fois.
- **traitement** : [[Schéma programmes ancien.canvas|Schéma programmes ancien]]
- **Création du Fortran**
- **3eme gen** : ~1960 : premieres protections et dossiers...
- **4eme gen** : ~1965 - 1975 : creation d'ordonnancement pour permettres a plusieurs taches d'etres effectutées en meme temps
- **4eme gen** : > 1975 : microprocesseurs, unix, macos...
- **5eme gen** : >1980 : Création de réseaux locaux et machines dédiées a une seule tache.

--- 
### Pourquoi améliorer ordinateurs ? : 
- Travailler le cpu de maniere optimale
- facile a programmer
- améliorer la compatibilité entre programmes et systemes.
- avoir la meilleure experience utilisateur

Les composants communiquent grace a des "systems bus", le bus permet de répartir la mémoire 

Chaque périphérique a un driver qui est inscrit dans le code de l'OS

Le cpu a 2 modes d'exec : mode user et mode kernel

Quand nouvel evenemnt : le cpu crée un nouveau mode

**Existence des evenements asynchrone :** 
- possibilité d'interrompre le programme en cours et d'en executer parallelement
- cpu cherche prochaine exec, teste si il y a un evenement, si il y en a un il execute le code mais va etre obligé d'interrompre le code qu'il exécutait
- un evenement peut etre une exception car erreur dans le code ou division par 0 ou panne périphérique ou appel systeme dans un programme donc interruption pour aller chercher la donnée avant de revenir au code.
  

**Les horloges** : permet de gérer les timers pour éviter les boucle infinies ou éviter qu'un programme prenne toute la mémoire.

Pour arreter un programme dans ce cas : timers qu'on peut déclancher si on est niveau kernel pour arreter le programme dans x temps.

les cpu ont du cache car demander acces mémoire trop long, cache tres petit et extremement rapide.

Processus : représente l'éxécution d'un code sous le controle de l'OS


**Comportement OS :** 
démarrage : bootstrap : charge en mémoire le kernel et initialise ensuite le systeme
le kernel attend des evenements, interrompt et execute.

--- 
### Execution des programmes : 
- l'OS doit pouvoir prendre le controle du cpu a tout moment pour arreter un processus.
- avoir un algo d'ordonnancement
- répartir la ram entre les programmes
- controler les programmes
- permettre a plusieurs programmes de partager du code et de la mémoire
- gérer le parallélisme


**Gestion de la mémoire :** 
programme toujours exécuté sur la mémoire, jamais sur le disque
passer des données de ram a disque

**Gestion des fichiers :** 
user doit pouvoir stockers fichiers
doit pouvoir créer, détruire, partager...

**Gestion entrees sorties :** 
e/s lentes par rapport au cpu.

--- 
### interface user :
- fournir gestion des fichiers
- charger des executables en mémoire
- traitement d'erreurs
- permettre au user d'intervenir dans le déroulement des programme
- fournir des outils permettant de gérer le réseau
- gérer les utilisateurs
- permettre des mises a jour et sauvegardes réguliere de tout les fichiers
- controler les performances
- fournir un shell

--- 
### Sécurité : 
- processus ne doivent pas interferer entre eux ou avec le systeme
- une ressource possède une gestion des droits d'acces pour les autre utilisateurs et processus
- doit fournir une protection contre les intrusions, virus...
- fournir un systeme d'authentification
	- chaque utilisateur est lié a un numéro
	- pouvoir créer un groupe et gérer les permissions de celui-ci
		- permet de garder des logs de qui s'est connecté et ce que celui-ci a fait
- l'OS possède une "acces control list" qui sait quels sont les permissions de chaque fichier (chmod etc...)
- donner des droits temporaires ( je lance un programme je veux pouvoir modifier la base de données mais pas lorsque mon programme n'est pas lancé )

possibilité de faire des appels systemes dans des languages de programmation mais plus long ( ex python avec os )
Le c a été développé en meme temps qu'unix pour assurer la portabilité

**structure de unix :** 
![[Schéma unix]]

--- 
### Shells :
- permet de communiquer avec le systeme
- nous utiliserons le shell
- ```man```
	- [] -> optionnel
	-  | -> soit l'un soit l'autre mais pas les deux
	- ... -> plusieurs options possibles ( ex : fichier 1 fichier 2... )
	- souligné -> obligatoire
	- peu importe l'ordre
- language bas niveau permet d'automatiser des taches du systeme
- renvoie 0 si la commande s'est bien passé sinon un entier >0

--- 
### Fichiers :

^77c915

^50ea0f
- **types** :
	- fichiers ordinaires ( - ) -> sur le disque
	- liens symobliques ( 1 ) -> raccourcis
	- fichiers spéciaux ( b ou c ) -> périphériques
	- répertoires ( d )
- **Unix** : bin usr etc users dev tmp [[schéma fichiers unix.canvas|schéma fichiers unix]]
	- / -> racine
	- /bin et usr/bin/ -> commandes unix
	- usr/local/bin -> commandes particulières
	- /tmp -> fichiers temporaires
	- /etc -> commande d'administration
	- /dev -> gestions périphériques
	- /users ou /home-> répertoire d'acceuil pour les utilisateurs
- Désignation **relative** -> on part de notre répertoire
- Désignation **absolue** -> on part de la racine

--- 
### Droits :
- tout utilisateur a un login et un groupe
- chaque fichier a 3 classes d'utilisateur :
	- u -> user
	- g -> group
	- o -> other
- **types de droits :**
	- r -> read
	- w -> write
	- x -> execute
- ajout et supression des fichiers est gérée par les droits du répertoire et non du fichier lui-meme
- ```
  ls -l ...
  ```
  -> renvoie les droits du fichier ou du répertoire
	- dans l'ordre : 
		- lien
		- 3 premiers carac pour user
		- 3 d'apres group
		- et 3 derniers other
		- nombre de liens
		- propriétaire
### Liens
- **lien physique** donne un autre nom a un meme fichier
	- ```
	  ln source destination
	  ```
	- meme si on supprime source, destination existera toujours 
- **lien symbolique** est un raccourcis
	- ```
	  ln -s source destination
	  ```

### Occupation disque
- ```
  df -k (mais -h donne l'unité la plus appropriée)
  ```
  -> donne des infos sur la place disponible en ko