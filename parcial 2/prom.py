#Arnold Merchan
#4 Desarrollar un algoritmo que calcule el promedio de un arreglo de reales
Nelem=int(input('ingrese numero de elementos'))
lista=[]
for i in range(Nelem):
    elemento=input('ingrese elemento')
    lista.append(elemento)
    s=float(0)
    for i in lista:
        x=float(i)
        s+=x

prom=s/Nelem
print(f'el promwedio de los datos ingresados es{prom}')

