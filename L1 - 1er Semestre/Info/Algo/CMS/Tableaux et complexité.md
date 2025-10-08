# Résumé – CM3 : Tableaux & Complexité

## 1. Tableaux et Matrices

### Spécifier un type
- Un type est défini par :
  - un **espace de valeurs**
  - un **ensemble d’opérations autorisées**
- **Type abstrait** = définition logique d’un type (indépendante de l’implémentation)
- **Structure de données** = implémentation concrète en mémoire

### Motivation
- Objectif : manipuler des **séquences d’éléments**
- Pourquoi pas utiliser `list` en Python ?
  - Trop spécifique au langage
  - Trop de fonctionnalités inutiles
- On cherche un **ensemble minimal d’opérations** disponible dans la plupart des langages

### Type abstrait Tableau
- Caractéristiques :
  - Nombre d’éléments fixe
  - Tous les éléments du même type
  - Accès par **indice**
- Opérations autorisées :
  - Créer un tableau
  - Connaître la longueur
  - Lire un élément
  - Remplacer un élément

```python
# Exemple Python
def creer_tableau(longueur, defaut):
    return [defaut] * longueur

tab = creer_tableau(20, 0)
tab[0] = 5
tab[1] = 2 * tab[0]
```
```C
// Exemple C
int tableau[20] = {0};
scanf("%d", &tableau[0]);
tableau[1] = 2 * tableau[0];
```

### Type abstrait Matrice

- **Caractéristiques** :
  - Tableau à deux dimensions
  - Nombre de lignes et colonnes fixé
  - Tous les éléments du même type

- **Opérations autorisées** :
  - Créer une matrice
  - Connaître dimensions
  - Lire un élément
  - Remplacer un élément

```python
# Exemple Python
def creer_matrice(nb_lignes, nb_colonnes, defaut):
    return [[defaut] * nb_colonnes for _ in range(nb_lignes)]

mat = creer_matrice(19, 13, 0)
mat[3][4] = 7
mat[2][7] = 2 * mat[3][4]
```
<<<<<<< HEAD:L1 - 1er Semestre/Info/Algo/Tableaux et complexité.md

```
=======
```C
>>>>>>> origin/main:L1 - 1er Semestre/Info/Algo/CMS/Tableaux et complexité.md
// Exemple C
int matrice[19][13] = {0};
scanf("%d", &matrice[3][4]);
matrice[2][7] = 2 * matrice[3][4];
```

## 2. Complexité

### Définition
- Complexité = ressources nécessaires selon la taille de l’entrée
- Ressources :
  - **Temps** (opérations)
  - **Mémoire**
- Taille de l’entrée : longueur d’un tableau, valeur d’un entier…

### Exemple : Somme des entiers
- `for` de 1 à n → **O(n)**
- Formule `n(n+1)/2` → **O(1)**

```python
# Exemple Python
def somme_entiers_1(n):
    somme = 0
    for i in range(1, n+1):
        somme += i
    return somme

def somme_entiers_2(n):
    return n * (n+1) // 2
```

### Observation expérimentale
- Mesurer le temps avec `time.time()`
- Temps d’exécution croît proportionnellement à `n`
- Complexité confirmée : **linéaire**

### Application : Racine carrée entière
- Problème : trouver `a` tel que `a² ≤ n < (a+1)²`
- Algorithme 1 : balayage → **O(√n)**
- Algorithme 2 : dichotomie → **O(log n)**

```python
# Balayage
def racine_entiere_1(n):
    assert n >= 0
    a = 0
    while (a+1)**2 <= n:
        a += 1
    return a


# Dichotomie
def racine_entiere_2(n):
    assert n >= 0
    a, b = 0, n+1
    while b - a > 1:
        m = (a+b)//2
        if m**2 <= n:
            a = m
        else:
            b = m
    return a
```

### Complexités usuelles
- Parcours linéaire tableau → **O(n)**
- Boucles imbriquées → **O(n²)**
- Parcours matrice `nl × nc` → **O(nl · nc)**
- Recherche dichotomique → **O(log n)**
- Tri quadratique (insertion, sélection) → **O(n²)**
- Tri efficace (fusion, rapide) → **O(n log n)**
