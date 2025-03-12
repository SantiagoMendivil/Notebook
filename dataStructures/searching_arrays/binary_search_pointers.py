def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid  # Se encontró el elemento, devolver índice
        elif arr[mid] < target:
            left = mid + 1  # Mover el puntero izquierdo
        else:
            right = mid - 1  # Mover el puntero derecho

    return -1  # No se encontró el elemento


# Ejemplo de uso
arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7
result = binary_search(arr, target)

if result != -1:
    print(f"El elemento {target} se encuentra en el índice {result}.")
else:
    print(f"El elemento {target} no está en la lista.")
