Ensemble de ressources :
- **matérielles et logicielles** :
	- RJ45, Courant électrique, Fibre optique, Ondes (wifi,3G,...)

Deux modèles réseaux :
- OSI et TCP/IP

### Role des réseaux :
- **Partage** de ressources 
- Communication entre :
	- personnes (messagerie électronique, travail collaboratif, forums, blogs, réseaux sociaux, etc.)
	- processus (ordinateurs industriels…)
- Réduction de coût : plusieurs micro-ordinateurs remplacent un gros
- Garantie de l'unicité et de l'universalité de l'accès à l'information (bases de données en réseau
- Fiabilité/résistance aux pannes (duplication des données)
- Commerce électronique
- Jeux en réseaux 

--- 
### Avantages :
- Communication et organisation plus efficace
- Diminution des couts
- Standardisation des applications
- Accès aux données en temps réel

--- 
### Propriétes
- Portée : atteindre un maximum de sites
- Débits élevés
- Simplicité d'utilisation
- Robustesse et disponibilité
- Sécurité renforcée pour certaines applications
- Bon temps de réponse
- Facilité d'évolution
- Couts faibles

--- 
### Classification :
- PAN : Réseau personnel
- LAN : Réseau d'entreprise
- MAN : Couvre une vile
- WAN : Un pays ou un continent
- Fils :
	- Cable torsadé
	- Cable coaxial
	- Fibre optique
	
![[Pasted image 20250924135500.png]]

---
### Transmissions sans fil
- **Wifi :**
	- Limité à 100mb/s dans la pratique
	- Portée de quelques dizaines de metres à quelques centaines de mètres
- **Bluethooth :**
	- Faible consommation comparé au wifi
	- WPAN
	- Débit théorique de 3mb/s
	- Faible portée
- **Infra-rouge :**
	- WPAN
	- Débits plus ou moins importants ( 10mb/s )
	- Emetteur et récepteur doivent etre visibles l'un de l'autre
	- Tres courte distance

--- 
### Topologie :
- Un réseau est composé de :
	- **Terminaux** ( au sens informatique --> ordinateur )
	- **Noeuds** ( commutateur )
	- **Liens** : liens physiques entre les noeuds et les terminaux
- A diffusion :
	- Un lien partagé relie les liens entre eux ainsi qu'avec le terminal
	- Un message envoyé sur un canal ets reçu par toutes les relations
- *voir [[Cours-Réseaux.pdf]] pour examples*

---
### Relations
- #### Client / Serveur :
	- Client demande informations au serveur et celui-ci va interroger base de données ou autre et serveur va écrire une réponse au client
	- **Avantages :**
		- Centralisation des données
	- **Inconvénients :**
		- Le serveur doit etre puissant
		- Le débit doit etre important
	- **Remède :**
		- Créer des sites mirroirs identiques comme ca meme si un tombe en panne --> pas de probleme
- #### Peer to Peer :
	- Toutes les machines ont le meme niveau dans le réseau et vont en meme temps émettre en meme temps recevoir --> Servant ( chacun est soit serveur soit client )
	- **Exemples** :
		- Partage de fichier
		- Skype
		- Le streaming
		- Mise en commun de puissance de calcul
	- **Avantages :**
		- Plus un objet est populaire plus il est disponible
		- Robustesse : censure ou attaque plus difficile
		- Plus un fichier est demandé, le noeud qui possédait cette information recoit moins de charge car l'information se duplique chez les autres noeuds
		- Décentralisation de services
	- **Inconvénients :**
		- Temps de réponse plus lents

---
### Transfert de fichier 
- Exemple TCP/IP :
	- La source (site sur lequel se trouve le fichier) demande l’activation de la communication au site destinataire 
	- Le destinataire accepte l’établissement de la communication avec la source
	- La source vérifie que le destinataire est prêt à recevoir le fichier
	- Le destinataire s’assure qu’il a suffisamment d’espace mémoire pour stocker le fichier
	- La source envoie le fichier morceau par morceau
	- Le destinataire recevoit le fichier morceau par morceau
	- La source s’assure que tous les morceaux sont bien reçus
	- Le destinataire acquitte la réception des morceaux successifs 

--- 
### Transmission de messages
- **l'Adresse peut etre :**
	- Un nom logique ( adresse ip ou nom personnalisé )
	- Un nom physique ( adresse MAC )
- **Routage :**
	- Le chemin peut changer si un noeud est obsolète
- **TCP/IP :**
	- Protocole TCP ajoute un en-tete avec :
		- Port d'origine, port de destination
	- Chaque paquet est encadré par 2 entetes, un tcp et un ip
	- IP vérifie la destination et TCP envoie au logiciel concerné

--- 
### Différents types d'adresses :
- IPV4, IPV6
- Adresse FQDN ( nom @ domaine . pays du domaine )
- URL 
- MAC --> associée a une carte réseau, donne une adresse unique imuable car physique
- **IPV4 :**
	- Environ maximum de 4 milliards d'adresse
	- Deux premier nombre : réseau local, deux derniers : adresse de la machine
	- Nombres compris entre 0 et 255
	- DNS est un service qui permet de retrouver une adresse IP à partir de l'adresse FQDN ou d'un lien 
		- Il va demander regarder le .fr donc aller en france puis regarder le domaine et interroger ce domaine en France donc
	- **Classes :**
		- A -> Réseaux avec beaucoup de machines ( adresse ip en binaire commence par 0 )
		- B -> Moyen reseaux ( pareil mais 01 )
		- C -> Petits réseaux ( pareil mais 10 )
- **IPV6 :**
	- héxadécimale ( base 16 )
	- 4 caractères séparés par des :
	- On peut regrouper les 0 en un seul si jamais il y a 4 zéros dans le meme groupe ex : ....:0000:... -> ....:0:....
	- Si il y a plusieurs fois des groupes nuls on peut rassembler en écrivant simplement des ":" mais on y a le droit qu'UNE SEULE FOIS exemple : 0000:0000:0000 -> :::