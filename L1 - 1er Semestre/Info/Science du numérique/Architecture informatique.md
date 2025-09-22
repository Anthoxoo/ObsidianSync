### Von neumann
mémoire reliée par des bus à l'unité centrale ( composée de l'unité arithmétique et logique et de l'unité de controle )

On a seulement acces a une machine virtuelle qui nous est donnée par l'intermédiaire des périphériques d'entrés et de sorties qui rend l'utilisation facile par tous crée par l'OS

Carte mère connecte tout les composants a l'aide de bus.
Unité arithmétique et logique est composée d'accumulateurs ( = cache) pour plus de rapidité

--- 
### Le microprocesseur peut : 
- acceder a la mémoire
- effectuer des opérations arithmétiques
- effectuer des opérations logiques
- controler des séquences et des branchements conditionnels ( = if, else, boucle for,while...)
- il possède aussi une horloge exprimée en hz
	- l'horloge permet de synchroniser les actions de la machine

### Mémoire
- capacité
- temps d'acces
- temps de cycle (= intervalle entre deyx demandes d'écriture / lecture )
- débit
- volatilité ( permanence ou non des infos ex : ram volatile, hdd non)
- classement de la mémoire en terme de vitesse ( lié à l'emplacement physique par rapport au microprocesseur ) :
	- registres ( minuscule -> 512 bits)
	- cache ( tres petit, de l1 à l3 - de 64bits à 64 mio)
	- mémoire principale ( RAM 64gio)
	- mémoire d'appui ( peu commun )
	- mémoire de masse ( hdd / ssd )
- différence ram et rom : rom est seulement lisible on ne peut pas écrire dessus, contient le bios et l'acces aux périphériques.
		--> il est tout de meme possible d'écrire dessus donc on efface tout et on réecrit.

### bus :
- 3 types de bus :
	- commandes donne des instructions a executer
	- adresses donne les endroits où ecrire en mémoire
	- information transport des données
- pci express, pci, ethernet, sata... Tout ca sont des bus

### chipset : 
- north bridge / south bridge
	- north est intégré souvent au microprocesseur et s'occupe des liaisons rapides

pilote permet a un périphérique physique de communiquer avec l'OS

### Execution de programme
- charge le programme en mémoire bout par bout car sinon trop gros
- transmettre a l'unité de commande l'application et les données a l'unité arithmétique et logique
- puis executer le code et le placer dans un registre particuler avant de tout renvoyer a la mémoire