#!/usr/bin/env python3

def eliminer_doublons(liste):
    i = 1
    while i<len(liste):
        while i < len(liste) and liste[i]==liste[i-1] :
            liste.pop(i)
            #PAS DE I+=1 
        i += 1

def eliminer_doublons2(liste):
    i = 1
    while i<len(liste):
        if liste[i]==liste[i-1] :
            liste.pop(i)
        else: 
            i += 1


def test_eliminer_doublons():
    print('Test de la fonction eliminer_doublons')
    liste = []
    assert eliminer_doublons(liste)==None and liste==[]
    liste = [7]
    assert eliminer_doublons(liste)==None and liste==[7]
    liste = [7,7]
    assert eliminer_doublons(liste)==None and liste==[7]
    liste = [7,9,10,2]
    assert eliminer_doublons(liste)==None and liste==[7,9,10,2]
    liste = [7,7,9,10,2]
    assert eliminer_doublons(liste)==None and liste==[7,9,10,2]
    liste = [7,9,10,2,2]
    assert eliminer_doublons(liste)==None and liste==[7,9,10,2]
    liste = [7,9,9,10,2]
    assert eliminer_doublons(liste)==None and liste==[7,9,10,2]
    liste = [7,9,9,10,9,9]
    assert eliminer_doublons(liste)==None and liste==[7,9,10,9]
    liste = [7,7,9,9,10,10,2,2]
    assert eliminer_doublons(liste)==None and liste==[7,9,10,2]
    liste = [7,9,10,2,2,2]
    assert eliminer_doublons(liste)==None and liste==[7,9,10,2]
    print('  OK')

test_eliminer_doublons()