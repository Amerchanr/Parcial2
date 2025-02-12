#Arnold Merchan
#El programa determina si hay elementos repetidos

Nelem=int(input('ingrese numero de elementos'))
lista=[]
for i in range(Nelem):
    elemento=input('ingrese elemento')
    lista.append(elemento)

for i in lista:
    
    contador=lista.count(i)
    
    if contador>1:
        print(f'el elemento {i} se encuentra repetido {contador} veces')
    else:
        print('no hay elementos reperidos')



