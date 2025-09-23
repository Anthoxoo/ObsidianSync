#!/usr/bin/env python3

def mystere_1(liste,n):
    ...

def test_mystere_1():
    print('Test de la fonction mystere_1')
    liste = []
    assert mystere_1(liste,0)==[]
    assert mystere_1(liste,7)==[]
    assert mystere_1(liste,-5)==[]
    assert liste == []
    liste = [9]
    assert mystere_1(liste,0)==[9]
    assert mystere_1(liste,7)==[9]
    assert mystere_1(liste,-5)==[9]
    assert liste == [9]
    liste = [7,4]
    assert mystere_1(liste,0)==[7,4]
    assert mystere_1(liste,13)==[4,7]
    assert mystere_1(liste,-6)==[7,4]
    assert liste == [7,4]
    liste = [9,5,10]
    assert mystere_1(liste,0)==[9,5,10]
    assert mystere_1(liste,1)==[5,10,9]
    assert mystere_1(liste,2) == [10,9,5]
    assert mystere_1(liste,3) == [9,5,10]
    assert mystere_1(liste,4) == [5,10,9]
    assert mystere_1(liste,-1)==[10,9,5]
    assert liste == [9,5,10]
    liste = [8,5,6,13,2,8]
    assert mystere_1(liste,0)==[8,5,6,13,2,8]
    assert mystere_1(liste,1)==[5,6,13,2,8,8]
    assert mystere_1(liste,-1)==[8,8,5,6,13,2]
    assert mystere_1(liste,5)==[8,8,5,6,13,2]
    assert mystere_1(liste,-5)==[5,6,13,2,8,8]
    assert mystere_1(liste,8)==[6,13,2,8,8,5]
    assert mystere_1(liste,40)==[2,8,8,5,6,13]
    assert mystere_1(liste,-666)==[8,5,6,13,2,8]
    assert mystere_1(liste,60000000000000000000000000000)==[8,5,6,13,2,8]
    assert liste==[8,5,6,13,2,8]
    print('  OK')

def mystere_2(liste,n):
    ...

def test_mystere_2():
    print('Test de la fonction mystere_2')
    liste = []
    assert mystere_2(liste,7)==None and liste==[]
    liste = [9]
    assert mystere_2(liste,7)==None and liste==[9]
    liste = [8,5,6,13,2,8]
    assert mystere_2(liste,0)==None and liste==[8,5,6,13,2,8]
    assert mystere_2(liste,1)==None and liste==[5,6,13,2,8,8]
    assert mystere_2(liste,-1)==None and liste==[8,5,6,13,2,8]
    assert mystere_2(liste,5)==None and liste==[8,8,5,6,13,2]
    assert mystere_2(liste,-5)==None and liste==[8,5,6,13,2,8]
    assert mystere_2(liste,8)==None and liste==[6,13,2,8,8,5]
    assert mystere_2(liste,40)==None and liste==[8,5,6,13,2,8]
    assert mystere_2(liste,-666)==None and liste==[8,5,6,13,2,8]
    assert mystere_2(liste,60000000000000000000000000000)==None and liste==[8,5,6,13,2,8]
    print('  OK')

test_mystere_1()
test_mystere_2()