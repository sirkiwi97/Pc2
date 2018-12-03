n=[]
m=[]

while len(n)<5:
    n.append(int(input('num')))
def orden_menor(lista):
    menor=lista[0]
    for i in lista:
        if i < menor:
            menor=i
    m.append(menor)
    n.remove(menor)
    for i in lista:
        if i < menor:
            menor=i
    m.append(menor)
    n.remove(menor)        
    return menor
menor=orden_menor(n)
print (menor)
print(n)
print (m)