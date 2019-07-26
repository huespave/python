# Funcion número perfecto
def n_perfecto(x):
    cont=0
    for y in range(1, x): 
        if (x % y)==0:
            cont=cont+y
    if (cont==x):
        print("Numero perfecto",x)
    else:
        print("Numero NO perfecto",x)
n_perfecto(6)
n_perfecto(100)