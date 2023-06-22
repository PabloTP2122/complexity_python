import time
# Para ampliar el límite de recursión
import sys

numero_limite = 1500
sys.setrecursionlimit(numero_limite)

def factorial(n):
    respuesta = 1

    while n > 1:
        respuesta *= n
        n -= 1
    
    return respuesta

def factorial_r(n):
    if n ==1:
        return 1
    return n* factorial_r(n-1)

# Entry point
if __name__ == '__main__':
    n = 1000
    comienzo = time.time()
    factorial(n)
    final = time.time()
    print('Función factorial: ', final-comienzo)

    comienzo = time.time()
    factorial_r(n)
    final = time.time()
    print('Función recursiva: ', final-comienzo)