# Exercice 1
## 1 -
### a)
type du paramètre : entier positif
retour : pareil 
pré condition : n>=0
post condition : s=(n(n+1))//2
### b)
Invariant de boucle : s=(k(k+1))//2 and k=n 

## 2 - 
n-k car : entier strictement decroissant, positif ou nul en début de boucle.

# Exercice 2
## 1 - 
entrée : entier positif
retour : entier positif
précondition : n>0
post condition : k>=0 and 2** k<=n<2** (k+1)

## 2 - 
condition d'arret : n<2**(k+1)
condition de boucle : n>2**(k+1)

## 4 -
variant : n-k

# Exercice 4
## 1 -
### a)
```python
def auxi(l):  
    for i in range(1,len(l)):  
        if l[i-1] > l[i]:  
            return False  
    return True
```

### b)
précondition est dernier : len(tab)>0, tab\[0]<=0, tab\[len(tab)-1]>0

### c)
postcondition : 0<=i<len(tab)-1 tab\[i] <=0 tab\[i+1] > 0

## 2 -
### a)
condition d'arret : tab\[i+1] > 0
condition de boucle : tab\[i+1] <=0

## 3 -
Variant : len(tab)-i
il est bien entier décroissant et positif ou nul en début de boucle.

# Exercice 4 
Variant : j-i