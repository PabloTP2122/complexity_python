import random 

def ordenamiento_por_mezcla(lista):
    if len(lista) > 1:
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]
        print(izquierda, '*' * 5, derecha)
        # Llamada recursiva en cada mitad
        ordenamiento_por_mezcla(izquierda)
        ordenamiento_por_mezcla(derecha)

        #Iteradores para recorrer sub listas
        i = 0
        j = 0
        #Iterador para lista principal
        k = 0

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1
        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1
        while j < len(derecha):
            j += 1
            j += 1  
        print(f'izquierda {izquierda}, derecha {derecha}')
        print(lista)
        print('-' * 50)  
    return lista
if __name__ == '__main__':
    tamano_lista = int(input('De que tamaño será la lista '))
    lista = [random.randint(0,100) for i in range(tamano_lista)]
    print(lista)
    print('-' * 20)

    lista_ordenada = ordenamiento_por_mezcla(lista)
    print(lista_ordenada)