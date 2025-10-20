**Logiciel** = programme = suite d’instructions écrites dans un langage de programmation

Ordre **compilation**
[[Schéma code source vers binaire.canvas|Schéma code source vers binaire]]

**Décompilation** est sensiblement la meme chose mais on perd qqs trucs

**Chaine de production d'un programme** :

![[Chaine de production d'un programme.png]]

--- 
### Modules

- **Module** = fichier source :
	- implémente des fonctionnalités / services supplémentaires 
- **Module statique** = code objet dépendant du logiciel 
	- logiciel + Module = 1 fichier exécutable unique • 
- **Module dynamique** = code objet indépendant du logiciel 
	- logiciel = 1 fichier exécutable
	- module = 1 autre fichier exécutable

--- 
### Cout
- **cout de développement élevé** ( payer ingénieurs etc )
- **cout de prod faible** car juste a recopier code sur support

--- 
### Producteurs
- entreprises, développeurs indépendants
- qui vivent de l’exploitation commerciale du logiciel (vente, installation, conseil en ligne, formation, SAV…)

--- 
### Juridique
- Programme lui-même PROTECTION PAR LE **DROIT D’AUTEUR**
	- droits moraux
	- il faut que ce soit une oeuvre de l'esprit **original** afin de bénéficier du droit d'auteur
	- respecté au niveau international
	- respecté jusqu'à 70 ans après la mort de l'auteur
- Effet du Programme PROTECTION PAR LE **BREVET**
	- contrat de 20 ans entre société et inventeur
	- architecture, code source, code objet... protégés
	- pas possible en europe
- Contrat avec l’utilisateur PROTECTION PAR UNE **LICENCE**
	- contrat entre titulaire de la license et utilisateur
	- license d'utilisation imposée par le titulaire de la license
	- license **propriétaire** impose restriction sur les droits des utilisateurs
		- décompilation autorisée en Europe mais interdite aux USA si jamais pas de closes au préalable
		- Attention différence entre gratuit et libre !
- Emergence des **logiciels libres et open source**
	- cout elevés des licenses proprio
	- culturel -> facon de penser disant algo devraient etres dans le domaine public
	- le secret est un frein a la diffusion des idée et du développement du domaine
	- **license MIT** -> license extremement libre et tres utilisée car demande seulement de mentionner l'auteur
	- FSF = Free Software Fondation
	- Libertés garanties par license libres :
		- executer le programme pour tous les usages
		- éudier le fonctionnement du programme et l'adapter a ses besoins
		- copier le logiciel et le redistribuer
		- améliorer le programme et publier ces améliorations pour en faire profiter la communauté
	- **copyleft** = impose que le logiciel redistribué conserve la meme license après modification
	- **license contaminante** = si je prends un bout de code d'une license contaminante alors tout mon code devra etre sous la meme license que le code source pris
	- alternatives de licenses américaines en francais -> CeCILL 
		- respecte le droit francais et si litige, on regle selon la loi francaise
		- permet la compatibilité avec gpl ( 70% du marché des licenses libres ) pour ne pas bloquer des projets
	- licenses 100% open source et non copylefté et non contaminantes ex : KDE ou Debian
	- logiciels open source sont en évolution constante grace a la communauté et projets tres fiables.
- **RGPD**
	- est actif sur tout le territoire européen
	- obligation de savoir le traitement des données des utilisateurs
	- toute entreprise est concerné mais il faut que cette entreprise soit implantée sur le territoire européen ou alors qu'elle cible les citoyens de l'union européenne