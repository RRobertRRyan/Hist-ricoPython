
def obter_numeros_pares(lista_inteiros):
  """
  Retorna uma nova lista contendo apenas os números pares de uma lista original.

  Args:
    lista_inteiros: Uma lista de números inteiros.

  Returns:
    Uma nova lista com os números pares da lista de entrada.
  """
  numeros_pares = []
  
  for numero in lista_inteiros:

    if numero % 2 == 0:

      numeros_pares.append(numero)
      
  return numeros_pares


lista_original_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Lista original: {lista_original_1}")
print(f"Números pares: {obter_numeros_pares(lista_original_1)}")

lista_original_2 = [15, 22, 31, 40, 57, 68]
print(f"\nLista original: {lista_original_2}")
print(f"Números pares: {obter_numeros_pares(lista_original_2)}")

lista_vazia = []
print(f"\nLista original: {lista_vazia}")
print(f"Números pares: {obter_numeros_pares(lista_vazia)}")
