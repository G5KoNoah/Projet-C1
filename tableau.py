
def tableau(x,y,t):
    tab = [[0] * t] * t
    tab[0][1] = 1
    for i in range(len(tab)):
        print(tab[i])
    return tab


print(tableau(1,1,3))