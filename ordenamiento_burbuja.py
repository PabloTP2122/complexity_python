import random

# Ordenar elementos de una lista
def ordenamiento_de_burbuja(lista):
    # Longitud de la lista par iterar
    n = len(lista)

    # Debido a aque es un for dentro de otro 
    # la complejidad algoritmica es O(n*n) = O(n^2)
    for i in range(n): #O(n)
        for j in range(0, n - i - 1):#O(n), con anterior O(n)*O(n) = O(n^2)
            # Si el elemento anterior es mayor
            if lista[j] > lista[j + 1]:
                # Intercambio de elementos usando swaping
                lista[j], lista[j + 1 ] = lista[j+1], lista[j]
    
    return lista



if __name__ == '__main__':
    tamano_lista = int(input('Ingresa el tamaño de la lista '))

    # Lista a ordenar
    lista = [random.randint(0, 100) for i in range(tamano_lista)] # O (n)
    print(lista)

    lista_ordenada = ordenamiento_de_burbuja(lista)
    print(lista_ordenada)

    
