#Arnold Merchan
##Programa que dadas dos listas determine que elementos tiene la primera lista que no tenga la segunda
def list_auto():
    Nelem=int(input('ingrese numero de elementos'))
    lista=[]
    for i in range(Nelem):
        elemento=input('ingrese elemento')
        lista.append(elemento)
    return lista 

lista1=list_auto()
lista2=list_auto()

for i in lista1:
    elemento1=i
    if elemento1 in lista2:
        print(f'el elemento {elemento1} se encuentra en ambos arreglos')
    else:
        print(f'el elmento {elemento1} solo se encuentra en el arreglo 1')    
print(lista1)
print(lista2)