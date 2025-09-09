
def elementos_comuns(lista1, lista2):
    """
    Retorna uma lista com os elemntos que são comuns a duas listas.

    Args:
    lista1: A primeira lista d entrada.
    lista2: A segunda lista de entrada.

    Returns:
    Uma nova lista contendo os elementos que aparecem em ambos as alistas.
    
    """
    lista_comum = []

    for elemento in lista1:
        if elemento in lista2:
            lista_comum.append(elemento)
    
    return lista_comum

lista_a = [1, 2, 3, 4, 5]
lista_b = [4, 5, 6, 7, 8]
print(f"Os elementos comuns entre {lista_a} e {lista_b} são: {elementos_comuns(lista_a, lista_b)}")

lista_c = ["laranja", "banana", "maçã"]
lista_d = ["maçã", "uva", "abacaxi"]
print(f"Os elementos comuns entre {lista_c} e {lista_d} são: {elementos_comuns(lista_c, lista_d)}")

lista_e = [10, 20, 30]
lista_f = [40, 50, 60]
print(f"Os elementos comuns entre {lista_e} e {lista_f} são: {elementos_comuns(lista_e, lista_f)}")