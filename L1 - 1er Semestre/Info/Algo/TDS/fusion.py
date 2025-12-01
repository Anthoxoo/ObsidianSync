def est_vide():
    pass

def partager(liste):
    if est_vide(liste):
        return liste,liste
    t1,q = tete(liste),queue(liste)
    if est_vide(q):
        return liste,creer_liste_vide()
    t2, qq= tete(queue(liste)),queue(q)
    qq1,qq2 = partager(qq)
    return creer_liste(t1,qq1),creer_liste(t2,qq2)


def fusion(l1,l2):
    if est_vide(l1):
        return l2
    if est_vide(l2):
        return l1
    t1,q1 = tete(l1),queue(l1)
    t2,q2 = tete(l2),queue(l2)
    if t1 <= t2:
        return creer_liste(t1,fusion(q1,l2))
    else:
        return creer_liste(t2,fusion(l1,q2))
    

def tri_fusion(liste):
    if est_vide(liste) or est_vide(queue(liste)):
        return liste
    gauche,droite = partager(liste)
    gauche_triee = tri_fusion(gauche)
    droite_triee = tri_fusion(gauche)
    return fusion(gauche_triee,droite_triee)