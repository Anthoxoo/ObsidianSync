# Invariants

**Invariant --> 1 dans l'initialisation, dans la boucle**
## Par baleyage
Un invariant est quelque chose qui quelque soit la partie du code ou l'on est, celle-ci sera vraie
Exemple avec la division euclidienne par baleyage :

```python
def division_eucli(a,b):
	assert (a>=0 and b >0)
	q,r = 0,a
	assert (a==q*b+r and 0<=r) #Invariant de l'initialisation
	while r >=b:
		q,r=q+1,r-b
		assert(a==q*b+r and 0<=r) #Invariant
	assert(a==q*b+r and 0<=r<b)
	return q,r
```

Lorsque l'on a un baleyage, l'invariant est en partie ou completement compris dans la post-condition mais sans le n+1 car on vérifie que ca marche a chaque itération

## Par dichotomie
```python
def racine_entiere(n):
	assert n >= 0
	a = 0
	b = n + 1
	assert a >= 0 and b >= 0 and a**2 <= n < b**2 # Invariant init
	while b - a > 1:
		m = (a + b) // 2
		if m * m <= n:
			a = m
		else:
			b = m
		assert a >= 0 and b >= 0 and a ** 2 <= n < b ** 2 # Invariant
	assert (a >= 0 and a ** 2 <= n < (a + 1) ** 2)
	assert (a >= 0 and a ** 2 <= n < b ** 2 and b == a + 1)
```

---
# Variant
Une boucle possède un variant, cela signifie que celle-ci se terminera. Un variant est : 
- **positif ou nul début de boucle**
- **Entier**
- **Positif**
- **Strictement décroissant**




VOIR CM pour mettre exemples et compléter.