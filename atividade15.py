
def soma_acumulada(lista_numeros):
    """
    Calcula a soma acumulada de uma lista de números.

    Args: 
    Lista_numeros: Uma lista de números inteiros ou flutuantes. 

    Returns:
    Uma nova lista onde cada elemento é a soma acumulada dos elementos da lista original até aquela posição.
    
    """


    soma = []

    soma_atual = 0 

    for numero in lista_numeros:
        soma_atual += numero
        soma.append(soma_atual)

    return soma

lista_1 = [1, 2, 3]
print(f"Lista original: {lista_1}")
print(f"Soma acumulada: {soma_acumulada(lista_1)}")

lista_2 = [10, 20, 30, 40]
print(f"\nLista original: {lista_2}")
print(f"Soma acumulada: {soma_acumulada(lista_2)}")

lista_3 = [5, -2, 8, 1]
print(f"\nLista original: {lista_3}")
print(f"Soma acumulada: {soma_acumulada(lista_3)}")

lista_vazia = []
print(f"\nLista original: {lista_vazia}")
print(f"Soma acumulada: {soma_acumulada(lista_vazia)}")
