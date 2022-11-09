#on defini un fonction fibo avec comme parametre le terme
def fibo(terme):
    #on initialise une liste qui contient les deux premier termes de la suite
    li=[0,1]
    #tant que la longueur de la liste est inferieur au terme plus 1
    while len(li) < terme + 1:
        #alors
        l=len(li)
        li.append(li[l-1]+li[l-2])
    return li[-1]

print(fibo(3))
