# número perfecto
for x in range(1, 1000): 
    cont=0
    for y in range(1, x): 
        if (x % y)==0:
            cont=cont+y
    if (cont==x):
        print("P:",cont)