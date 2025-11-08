## Exercice 1 :
*voir feuille pour les schémas ( important, va tomber au ds )*

calcul(0) = 0
calcul(1) = 1
calcul(2) = 3
calcul(3) = 6

## Exercice 2 :
1) il n'y a pas de condition d'arret donc la fonction ne s'arretera jamais.
2) ```python
   def est_pair(n):
	   if n == 0:
		   return False
		else:
			return not est_pair(n-1)
   ```

## Exercice 3 :
```python
def compter_premier(n):
	if n == 0:
		return 0
	else:
		if est_premier(n):
			return 1 + compter_premier(n-1)
		else:
			return compter_premier(n-1)
```
## Exercice 4 :
*Voir feuille*
## Exercice 5 :

*Voir feuille*

## Exercice 7 :
```python
def ajouter_constante(liste,constante):
	if est_vide(liste):
		return creer_liste_vide()
	else:
		nouvelle_queue = ajouter_constante(queue(liste),constante)
		return creer_liste(tete(liste)+constante,nouvelle_queue)
```

