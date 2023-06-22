import random

def busqueda_lineal(lista, objetivo):
    match = False # O (1)

    for elemento in lista: # O(n)
        if elemento == objetivo:
            match = True
            break
    # ¿Cómo se hace con list comprehensions?
    return match

if __name__ == '__main__':
    tamano_lista = int(input('Ingresa el tamaño de la lista '))
    objetivo = int(input('¿Cuál es el número a encontrar? '))

    lista = [random.randint(0, 100) for i in range(tamano_lista)] # O (n)
    encontrado = busqueda_lineal(lista, objetivo)
    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no está"} en la lista')

    
