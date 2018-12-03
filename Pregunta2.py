n=[]
m=[]

while len(n)<5:
    n.append(int(input('num')))
def orden_menor(lista):
    menor=lista[0]
    for i in lista:
        if i < menor:
            menor=i
    return menor
menor=orden_menor(n)
print (menor)
