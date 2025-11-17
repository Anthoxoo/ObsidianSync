La hauteur peut s'obtenir en faisant 1 ( la racine ) + max(hauteur a gauche, hauteur a droite )

On renvoie 0 lorsque l'abre est vide afin de simplifier les appels récursifs par la suite.

pour unpacker la racine, droite et gauche on peut faire ca : ( essayer de prendre l'habitude de faire comme ca. ) 
```python
r, g, d = racine(arbre), gauche(arbre), droite(arbre)
```

Fonction calcul hauteur : 
```python
def hauteur_arbre(arbre):
	if est_vide(arbre):
		return 0
	r, g, d = racine(arbre), gauche(arbre), droite(arbre)
	hauteur_g = hauteur_arbre(g)
	hauteur_d = hauteur_arbre(d)
	return 1 + hauteur_g if hauteur_g > hauteur_d else 1 + hauteur_d
```

Fonction ajouter a droite: 
```python
def ajouter_a_droite(arbre,valeur)
	if est_vide(arbre,valeur):
		return creer_arbre(valeur,creer_arbre(),creer_arbre())
	r, g, d = racine(arbre), gauche(arbre), droite(arbre)
	return creer_arbre(r,g,ajouter_a_droite(d,valeur))
```


Fonction parcours largeur :
```python
def parcours_largeur(arbre):
	#Utilisation d'une file à l'aide d'une liste python
	noeuds_a_traiter = [arbre]
	while len(noeuds_a_traiter) > 0:
		noeud = noeuds_a_traiter.pop(0)
		r, g, d = racine(arbre), gauche(arbre), droite(arbre)
		print(r,end=" ")
		noeuds_a_traiter.append(g)
		noeuds_a_traiter.append(d)
```

Fonction parcours profondeur ( préfixe, infixe, suffixe)
```python
def parcours_profondeur(arbre):
	if est_vide(arbre):
		return 0
	r, g, d = racine(arbre), gauche(arbre), droite(arbre)
	# préfixe print(r, end=" ")
	parcours_prefixe(g)
	# infixe print(r, end=" ")
	parcours_prefixe(d)
	# suffixe print(r, end=" ")
```