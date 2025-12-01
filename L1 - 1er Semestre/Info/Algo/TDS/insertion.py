def inserer_liste_triee(valeur,liste):
    if est_vide():
        return creer_liste(valeur,liste)
    t,q = tete(liste), queue(liste)
    if valeur<=t:
        return creer_liste(valeur,liste)
    return creer_liste(t,inserer_liste_triee(valeur,q))


def tri_insert_recurs(liste):
    if est_vide(liste):
        return liste
    t,q = tete(liste), queue(liste)
    q_triee = tri_insert_recurs(q)
    return inserer_liste_triee(t,q_triee)