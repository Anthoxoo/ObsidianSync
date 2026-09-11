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


