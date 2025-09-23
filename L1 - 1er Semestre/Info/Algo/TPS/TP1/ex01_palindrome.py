#!/usr/bin/env python3

def est_palindrome(mot):
    debut = 0
    fin = len(mot) - 1
    while debut <= fin:
        if not mot[debut] == mot[fin]:
            return False
        debut += 1
        fin -= 1
    return True


def test_est_palindrome():
    print('Test de la fonction palindrome')
    assert est_palindrome('kayak')==True
    assert est_palindrome('a')==True
    assert est_palindrome('abc')==False
    assert est_palindrome('abba') == True
    assert est_palindrome('')==True
    assert est_palindrome('abcdba')==False
    print('  OK')

test_est_palindrome()