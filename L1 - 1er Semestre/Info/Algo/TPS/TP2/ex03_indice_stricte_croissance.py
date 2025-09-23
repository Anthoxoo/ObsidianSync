#!/usr/bin/env python3

def verifie_pre_condition(liste):
    return (len(liste)>0) and (liste[len(liste)-1]>liste[0])

def verifie_post_condition(liste,i):
    return (i>0 and i<len(liste)) and (liste[i-1]<liste[i])

def indice_stricte_croissance(liste):
    assert verifie_pre_condition(liste), 'Pre-condition'
    i = 1
    while liste[i-1]>=liste[i]:
        i += 1
    assert verifie_post_condition(liste,i), 'Post-condition'
    return i

def test_verifie_pre_condition():
    print('Test de la fonction verifie_pre_condition')
    assert verifie_pre_condition([])==False
    assert verifie_pre_condition([5])==False
    assert verifie_pre_condition([5,2])==False
    assert verifie_pre_condition([2,2])==False
    assert verifie_pre_condition([2,5])==True
    assert verifie_pre_condition([8,4,2,-1,6,5,3,8,7])==False
    assert verifie_pre_condition([7,4,2,-1,6,5,3,8,7])==False
    assert verifie_pre_condition([7,4,2,-1,5,5,3,8,8])==True
    print('  OK')

def test_verifie_post_condition():
    print('Test de la fonction verifie_post_condition')
    assert verifie_post_condition([2,5],-3)==False
    assert verifie_post_condition([2,5],-1)==False
    assert verifie_post_condition([2,5],0)==False
    assert verifie_post_condition([2,5],1)==True
    assert verifie_post_condition([2,5],2)==False
    assert verifie_post_condition([2,5],3)==False
    assert verifie_post_condition([7,4,2,-1,5,5,3,8,8],-1)==False
    assert verifie_post_condition([7,4,2,-1,5,5,3,8,8],0)==False
    assert verifie_post_condition([7,4,2,-1,5,5,3,8,8],1)==False
    assert verifie_post_condition([7,4,2,-1,5,5,3,8,8],2)==False
    assert verifie_post_condition([7,4,2,-1,5,5,3,8,8],3)==False
    assert verifie_post_condition([7,4,2,-1,5,5,3,8,8],4)==True
    assert verifie_post_condition([7,4,2,-1,5,5,3,8,8],5)==False
    assert verifie_post_condition([7,4,2,-1,5,5,3,8,8],6)==False
    assert verifie_post_condition([7,4,2,-1,5,5,3,8,8],7)==True
    assert verifie_post_condition([7,4,2,-1,5,5,3,8,8],8)==False
    assert verifie_post_condition([7,4,2,-1,5,5,3,8,8],9)==False
    print('  OK')

def test_indice_stricte_croissance():
    print('Test de la fonction indice_stricte_croissance')
    assert indice_stricte_croissance([8,10])==1
    assert indice_stricte_croissance([1,10,9,8,7,6,5,4,3,2])==1
    assert indice_stricte_croissance([9,8,7,6,5,4,3,2,1,10])==9
    assert indice_stricte_croissance([9,1,8,2,7,3,6,4,5,10])in [2,4,6,8,9]
    print('  OK')

test_verifie_pre_condition()
test_verifie_post_condition()
test_indice_stricte_croissance()

