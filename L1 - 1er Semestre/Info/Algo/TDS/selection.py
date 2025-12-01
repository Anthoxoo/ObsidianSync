def echange(l,i,j):
    tmp = l[i]
    l[i] = l[j]
    l[j] = tmp

def tri_selec(tab):
    for i in range(len(tab)):
        min = i
        for j in range(i,len(tab)):
            if tab[j]<tab[min]:
                min = j
        echange(tab,i,min)
    return tab


l = [1,3,5,3,2,1,3,9,8,4,3]
print(tri_selec(l))