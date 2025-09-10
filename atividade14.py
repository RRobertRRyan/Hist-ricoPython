
def remover_duplicados(lista):
    """
    Remove elementos duplicados de uma lista e retorna uma nova lista com apenas os elementos únicos.

    Args: 
    Lista: A lista de entrada que pode conter elemnetos duplicados.

    Returns: 
    Uma nova lista contendo apenas os elementos únicos da lista original.

    """

    elementos_unicos = set(lista)

    return list(elementos_unicos)

lista_com_duplicados_1 = [1, 2, 2, 3, 4, 4, 5, 5]
print(f"Lista original: {lista_com_duplicados_1}")
print(f"Lista sem duplicados: {remover_duplicados(lista_com_duplicados_1)}")

lista_com_duplicados_2 = ["laranja", "banana", "maçã", "laranja", "uva"]
print(f"\nLista original: {lista_com_duplicados_2}")
print(f"Lista sem duplicados: {remover_duplicados(lista_com_duplicados_2)}")
