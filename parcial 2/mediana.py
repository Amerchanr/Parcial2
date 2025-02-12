#Arnold Merchan
##5 Desarrollar un algoruitmo que determine la mediana de un arreglo de enteros .
#  la medianaa es el numero que queda en la mitad del arreglo despues de ser ordenado

Nelem=int(input('ingrese numero de elementos'))
lista=[]
for i in range(Nelem):
    elemento=int(input('ingrese elemento'))
    lista.append(elemento)

    
listaord=sorted(lista)
print(listaord)
mitad=int((Nelem/2)-0.5)
mitad2=int(Nelem/2)
par=Nelem%2
print(f'mitad={mitad2}')

if par ==0:
    posterior=int(mitad2+1)
    num1=listaord(mitad2)
    nim2=listaord(posterior)
    prom=((num1+nim2)/2)
    print(f'la mediana de la lista es {prom}')
else:
    mediana=listaord[mitad]
    print(f'la dediana del arreglo es {mediana}')
   

    
