# HTML

HTML --> HyperText Markup Language n'est pas un language de programmation.
## Balises
- Une **Balise** sert a structurer le document, indiquer les différentes parties et a les faire apparaitre sous une **forme donnée**.
- Syntaxe : <nomBalise\>
- 2 **types** de balises :
	- **ouvrante / fermantes** ex: <h1\> aaa </h1\>
	- **auto-fermantes** ex : <img\>
- **Elément** = ensemble des balises ouvrantes + contenu + balise fermante.
- **type** : 
	- **inline** --> ne casse pas le flux du texte, s'écrit sur une ligne et prends seulement la partie nécéssaire à l'affichage de son contenu. ex: span (=conteneur en ligne.), img
	- **block** --> crée un nouveau bloc --> retour a la ligne et s'étale sur tout la largeur disponible. ex: div, p
	- **sémantique** --> seulement là pour mieux décrire, exemple : footer, main, body, header...
- On essaye d'**éviter** les **div** et les **span** au profit de **balises sémantiques** comme **section**, etc... Car ca donne plus d'information.
- Exercice : cf exercice.txt
- **table** --> crée un tableau
	- **titre** du tableau : \<caption>
	- **Titre de la ligne** du tableau : \<tr> (table row)
	- **élément** du tableau \<td>
	- **taille de la case** du tableau \<colspan="x">, \<rowspan>
- **Formulaires** :
	- \<form>
	- action="" --> **toujours** le mettre mais pas utile pour le moment, nous donne le **résultat** de la requete
	- method="" --> **pareil que action** mais sert donner la méthode de **transmission** (post ou get)
- Balises intéractives
	- **Input** :
		- permet de donner un champs de texte pour l'utilisateur
		- balise auto fermante
		- \<textarea> fait la meme chose sauf qu'elle est ouvrante, fermante.
	- **button**
		- type="**submit**" permet de faire un boutton d'**envoi**
		- **Select**
			- **name**="blabla"
			- on le combine a des \<**option**> qui donne les options possible pour notre select.
		- type="**radio**" --> un **seul** choix possibles
		- type="**checkbox**" --> **plusieurs** choix possibles
		- le fait de mettre **le meme name**="" sur les input oblige le fait qu'une **seule** valeur puisse être selectionnée --> respecte les **conventions** de \<**radio**>
		- **value**="blabla" --> est la valeur qui sera **renvoyée** au **serveur**
		- \<label for ="id du composant"> permet de spécifier un **nom plus clair** à notre input --> utile pour les **malvoyants** et les **robots**
## Attribut
- Un attribut permet d'ajouter une information complémentaire dans une balise.
- Syntaxe : attr="valeur" ex: src="image.png"
- Certains sont des booléens et peuvent etres activés ou désactivés.
- attributs universels :utilisable dans n'importe quel balise, ex : id, class

cf voir arborescence moodle !

## CSS
- Permet de sélectionner un **élément** ou un **grp** d'élément présent dans le html.
- **syntaxe** : nomSelecteur { propriété1: valeur1; propriété2: valeur2; }
- Les regles s'effectuent en **cascade**, si on a deux fois la modification d'une meme propriété, c'est la **derniere occurence** qui compte.
- **Selection** :
	- **nom de la balise** --> applique a **toutes** les occurences de cette balise.
	- par **id** : \#nom_id{}
	- par **class** : nom_class{}
	- **Combiner** les sélecteur : p.important va prendre toutes les occurences de paragraphes avec **comme** class **important**.
- **padding** = marge intérieure
- **flexbox** est une méthode de mise en page, les éléments se **rétractent** ou se **dilatent** pour occuper la place disponible. On tilise des **conteneur flex** et des **items flex**. On peut choisir un layout **vertical** ou **horizontal** (row / column)
- **tableau** :
	- **table-layout :**
		- **auto** --> la largeur du tableau dépend du contenu 
		- **fixed** --> choisi la taille du tableau et autre
	- **border-collapse :**
		- **separate** (défaut) --> bordures ne sont pas séparées
		- **collapse** --> colle toutes les cases et le fait ressembler a un tableau "classique" (c'est souvent ce qu'on va préferer)
	- On peut mettre du **padding** pour que le texte dans les cases soit plus **centré**



