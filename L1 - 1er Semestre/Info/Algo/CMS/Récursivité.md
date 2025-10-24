**SAVOIR FAIRE SCHEMA APPEL DE FONCTION FEUILLE CM5**

```python
def somme_chiffres(n):

	if n == 0:
		return 0
	# 1234 -> 123 | 4
	partie_gauche = n // 10
	partie_droite = n%10
	return partie_droite + somme_chiffres(partie_gauche)
```

# Listes chainées
Deux constructeurs : l'un crée une liste vide et l'autre crée une liste a partir de la tete d'une autre.

On a le droit : 
- d'accéder a la tete de la liste
- d'accéder a la queue de la liste
- déterminer si la liste est vide ou non