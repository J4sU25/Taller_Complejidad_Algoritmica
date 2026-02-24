def interseccion(lista1, lista2):
    return list(set(lista1) & set(lista2))




# Prueba
lista1 = [1, 2, 3, 4, 5]
lista2 = [3, 4, 5, 6, 7]


print(interseccion(lista1, lista2)) 
#Reto A
def interseccion(lista1, lista2):
    resultado = []


    for elemento1 in lista1:                    # Recorre lista1 → O(n)
        for elemento2 in lista2:                # Por cada elemento, recorre lista2 → O(m)
            if elemento1 == elemento2:          # Compara uno a uno
                if elemento1 not in resultado:  # Evita duplicados
                    resultado.append(elemento1)


    return resultado
lista1 = [1, 2, 3, 9, 5]
lista2 = [3, 4, 8, 6, 7]
print(interseccion(lista1, lista2))

#Reto B
def interseccion_set(lista1, lista2):
    set1 = set(lista1)   # Convierte lista1 a conjunto → O(n)
    set2 = set(lista2)   # Convierte lista2 a conjunto → O(m)
    return list(set1 & set2)
# Prueba
lista1 = [1, 2, 4, 9, 5]
lista2 = [1, 4, 8, 6, 7]


print(interseccion_set(lista1, lista2))  


def fibonacci(n):
    # Casos base
    if n < 0:
        raise ValueError("El número debe ser mayor o igual a 0")
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # Caso recursivo: F(n) = F(n-1) + F(n-2)
    return fibonacci(n - 1) + fibonacci(n - 2)


# Ejemplo de uso
for i in range(10):
    print(f"F({i}) = {fibonacci(i)}")


