import random

def matriz_fin(tam):
    matriz=[[]]
    c=0
    x=1
    while c<tam:
        while x<=tam:
            matriz[c]+=[x]
            x+=1
        if len(matriz)<tam:
            matriz+=[[]]
        c+=1
        x=1
    return matriz

def matriz_fin_trans(mat):
    n=0
    while n < len(mat):
        print(mat[n])
        n+=1
    print()
    print("-------------------------------------------")
    print()
    matriz=[[]]
    matriz=[[]]
    c=0
    x=0
    while c<len(mat):
        while x<len(mat):
            matriz[c]+=[mat[x][c]]
            x+=1
        if len(matriz)<len(mat):
            matriz+=[[]]
        c+=1
        x=0
    n=0
    while n < len(matriz):
        print(matriz[n])
        n+=1

    print()
    return matriz

def matriz_ini(tam):
    n=0
    while n < len(mat):
        print(mat[n])
        n+=1
    print()
    print("-------------------------------------------")
    print()
    matriz=[[]]
    c=0
    x=1
    while c<tam:
        while x<=tam:
            n=random.randint(0, tam)
            while n in matriz[c]:
                n=random.randint(0, tam)
            matriz[c]+=[n]
            x+=1
        if len(matriz)<tam:
            matriz+=[[]]
        c+=1
        x=1
    n=0
    while n < len(matriz):
        print(matriz[n])
        n+=1

    print()
    return matriz

def mat_tras(mat):
    n=0
    while n < len(mat):
        print(mat[n])
        n+=1
    mat_1=mat
    j=0
    i=0
    print()
    print("-------------------------------------------")
    print()
    while j<len(mat) :
        while i < len(mat[j]):
            mat_1[i][j]=mat[j][i]
            i+=1
        j+=1
        i=0
    n=0
    while n < len(mat_1):
        print(mat_1[n])
        n+=1

    print()
    return mat_1


