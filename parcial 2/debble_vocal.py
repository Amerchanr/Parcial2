#Arnold Merchan
#2 dedarrollar un programa que determine si en una lista se encuentra una cadena de caracteres con dos o mas vocales
# si la cadena existe debe imprimirla y si no existe debe imprimir no existe

Nelem=int(input('ingrese numero de elementos'))
lista=[]
for i in range(Nelem):
    elemento=input('ingrese cadena de caracteres')
    lista.append(elemento)
for i in lista:
    cadena_min=i.lower()
    A=i.count('a')
    E=i.count('e')
    I=i.count('i')
    O=i.count('o')
    U=i.count('u')
    sum=A+E+I+O+U
pocisioin=int(len(lista))
ultimo=lista[pocisioin-1]
if sum>2 :
    print(f'dentro de la cadena {i} hay mas de dos vocales')
elif i== ultimo:
    if sum<2:
        print('no existe')  

