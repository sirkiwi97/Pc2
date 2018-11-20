n1=int(input("Primer numero"))
n2=int(input("Segundo numero"))
n3=int(input("Tercer numero"))
n4=int(input("Cuarto numero"))
n5=int(input("Quinto numero"))

num=[]

def menor_en_arreglo (n1,n2,n3,n4,n5):
    if n1<n2 and n1<n3 and n1 <n4 and n1<n5:
        num.append(n1)
        if n2<n3 and n2<n4 and n3<n5:
            num.append(n2)
        elif n3<n2 and n3<n4 and n3<n5:
            num.append(n3)
        elif n4<n2 and n4<n3 and n4<n5:
            num.append(n4)
        else:
            num.append(n5)            

    elif n2<n1 and n2<n3 and n2<n4 and n2<n5:
        num.append(n2)
        if n1<n3 and n1<n4 and n1<n5:
            num.append(n1)
        elif n3<n1 and n3<n4 and n3<n5:
            num.append(n3)
        elif n4<n1 and n4<n3 and n4<n5:
            num.append(n4)
        else:
            num.append(n5)     


    elif n3<n1 and n3<n2 and n3<n4 and n3<n5:
        num.append(n3)
        if n1<n2 and n1<n4 and n1<n5:
            num.append(n2)
        elif n2<n3 and n2<n3 and n2<n5:
            num.append(n2)
        elif n4<n2 and n4<n3 and n4<n5:
            num.append(n4)
        else:
            num.append(n5)     

    elif n4<n1 and   n4<n2 and n4<n3 and n4<n5:
        num.append(n3)
        if n2<n3 and n2<n1 and n2<n5:
            num.append(n2)
        elif n3<n2 and n3<n1 and n3<n5:
            num.append(n3)
        elif n1<n2 and n1<n3 and n1<n5:
            num.append(n4)
        else:
            num.append(n5)    
    elif n5<n1 and n5<n2 and n5<n3 and n5<n4:
        num.append(n5)
        if n2<n3 and n2<n4 and n2<n1:
            num.append(n2)
        elif n3<n2 and n3<n4 and n3<n1:
            num.append(n3)
        elif n4<n2 and n4<n3 and n4<n1:
            num.append(n4)
        else:
            num.append(n1)    