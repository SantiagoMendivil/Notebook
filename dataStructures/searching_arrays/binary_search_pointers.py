def busqueda_binaria(lista_ordenada, puntero_izquierdo, puntero_derecho, valor):
    """Algoritmo de busqueda binaria usando punteros
    Args:
        :param lista_ordenada: Lista ordenada de elementos
        :param puntero_izquierdo: Indice inicial de la sub-lista 
        :param puntero_derecho: Indice final de la sub-lista
        :param valor: El valor a buscar en la lista

    Returns:
        :return: Indice de el valor si se encuentra, de otro modo "valor no encontrado"
    """
    # this condition indicates we've reached an empty "sub-list"
    if puntero_izquierdo >= puntero_derecho:
        return "valor no encontrado"
    # We calculate the middle index from the pointers now
    indice_medio = (puntero_izquierdo + puntero_derecho) // 2
    valor_medio = lista_ordenada[indice_medio]
    if valor_medio == valor:
        return indice_medio
    if valor_medio > valor:
        # we reduce the sub-list by passing in a new right_pointer
        return busqueda_binaria(lista_ordenada, puntero_izquierdo, indice_medio, valor)
    if valor_medio < valor:
        # we reduce the sub-list by passing in a new left_pointer
        return busqueda_binaria(lista_ordenada, indice_medio + 1, puntero_derecho, valor)


values = [77, 80, 102, 123, 288, 300, 540]
start_of_values = 0
end_of_values = len(values)
result = busqueda_binaria(values, start_of_values, end_of_values, 288)

print("element {0} is located at index {1}".format(288, result))
