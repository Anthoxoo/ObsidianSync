#!/usr/bin/env python3

def miroir_A(liste):
    result = []
    debut=0
    fin=len(liste)
    
    for i in range(fin-1,debut-1,-1):
        #print(i)
        result.append(liste[i])
    return result

def miroir_B(liste):
    temp = []
    for i in range(len(liste)):
        temp.append(liste.pop())
    liste = temp
    print(temp)
    
def miroir_C(liste):
    taille=len(liste)-1
    for i in range(len(liste)//2):
        temp = liste[i]
        liste[i]=liste[taille-i]
        liste[taille-i]=temp
        print(liste)
    return liste


def test_miroir_A():
    print('Test de la fonction miroir_A')
    liste = [1, 2, 3, 4, 5, 6, 7]
    assert miroir_A(liste)==[7, 6, 5, 4, 3, 2, 1] and liste==[1, 2, 3, 4, 5, 6, 7]
    liste = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10]
    assert miroir_A(liste)==[10, 9, 8, 7, 6, 5, 4, 2, 3, 1] and liste==[1, 3, 2, 4, 5, 6, 7, 8, 9, 10]
    liste = [0]
    assert miroir_A(liste)==[0] and liste==[0]
    liste = []
    assert miroir_A(liste)==[] and liste==[]
    print('  OK')

def test_miroir_B():
    print('Test de la fonction miroir_B')
    liste = [1, 2, 3, 4, 5, 6, 7]
    assert miroir_B(liste)==None and liste==[7, 6, 5, 4, 3, 2, 1]
    liste = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10]
    assert miroir_B(liste)==None and liste==[10, 9, 8, 7, 6, 5, 4, 2, 3, 1]
    liste = [0]
    assert miroir_B(liste)==None and liste==[0]
    liste = []
    assert miroir_B(liste)==None and liste==[]
    print('  OK')

test_miroir_A()
test_miroir_B()