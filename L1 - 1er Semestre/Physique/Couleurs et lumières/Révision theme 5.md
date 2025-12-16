### 1. La perception des couleurs en vision humaine

La perception des couleurs résulte de l'interaction entre la lumière et les cellules photosensibles de la rétine. Cette sensibilité est quantifiée par l'efficacité lumineuse relative spectrale, notée $V(\lambda)$.

- Vision diurne (Photopique) :
    
    Elle est assurée par les cônes, qui sont actifs lorsque la luminosité est suffisante.
    
    - Il existe environ 6 millions de cônes répartis de manière non uniforme.
        
    - L'œil humain est trichromate : il possède trois types de cônes ayant des maximums de sensibilité distincts à 420 nm ("bleu"), 533 nm ("vert") et 565 nm ("rouge").
        
    - La sensibilité globale de l'œil en vision diurne est maximale dans le jaune-vert à **555 nm**.
        
    - La perception finale de la couleur par le cerveau vient de la superposition des signaux envoyés par ces trois types de cônes.
        
- Vision nocturne (Scotopique) :
    
    Elle est assurée par les bâtonnets, beaucoup plus nombreux (100 à 110 millions) et bien plus sensibles (25 à 100 fois plus) que les cônes.
    
    - Il n'y a qu'un seul type de bâtonnet, ce qui ne permet pas de distinguer les couleurs (vision achromatique).
        
    - Leur pic de sensibilité est décalé vers le bleu, à **507 nm**.
        

### 2. La synthèse additive des couleurs

Ce principe, théorisé par Young, consiste à recomposer la lumière blanche ou toute autre couleur en additionnant des lumières colorées.

- Couleurs primaires et complémentaires :
    
    En superposant les trois lumières primaires (Rouge, Vert, Bleu), on obtient du blanc. En superposant deux primaires, on obtient la couleur complémentaire de la troisième:
    
    - **Rouge + Vert = Jaune** (complémentaire du Bleu).
        
    - **Vert + Bleu = Cyan** (complémentaire du Rouge).
        
    - **Rouge + Bleu = Magenta** (complémentaire du Vert).
        
- Distinction Longueur d'onde / Couleur :
    
    Il est important de noter que si une longueur d'onde monochromatique produit une sensation de couleur précise, la réciproque est fausse. Une même sensation de couleur (par exemple un jaune) peut être produite soit par une source monochromatique (une seule longueur d'onde), soit par un mélange de plusieurs longueurs d'onde (rouge + vert) qui stimulent les cônes de la même manière.
    

### 3. Les images numériques matricielles

Les images matricielles (ou bitmap) sont constituées d'un tableau de points appelés pixels.

- **Résolution et qualité :**
    
    - La résolution s'exprime souvent en **dpi** (dots per inch) ou ppp (points par pouce). Elle correspond au nombre de pixels par unité de longueur (1 pouce = 2,54 cm).
        
    - Une image est définie par sa hauteur et sa largeur en nombre de pixels.
        
- Poids et Codage (Profondeur) :
    
    Le poids d'une image dépend du nombre de pixels et du codage des couleurs, exprimé en bits par pixel (bpp).
    
    - **1 bpp :** Image en noir et blanc pur (2 états : 0 ou 1).
        
    - **8 bpp :** Permet 256 nuances, utilisé pour les niveaux de gris ou les "couleurs indexées" (palette prédéfinie de 256 couleurs pour alléger le fichier).
        
    - **24 bits (RVB) :** C'est le mode standard pour la couleur réaliste ("True Color"). Chaque canal (Rouge, Vert, Bleu) est codé sur 8 bits (256 nuances par canal), ce qui donne $256 \times 256 \times 256 \approx 16,7$ millions de couleurs possibles.