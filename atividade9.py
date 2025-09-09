
def eh_palindromo(frase):
  """
  Verifica se uma string é um palíndromo (lida da mesma forma de trás para frente).

  Args:
    frase: A string a ser verificada.

  Returns:
    True se for um palíndromo, False caso contrário.
  """
  # 1. Trata a string, removendo espaços e convertendo para minúsculas
  frase_tratada = frase.replace(" ", "").lower()

  # 2. Inverte a string tratada usando fatiamento
  frase_invertida = frase_tratada[::-1]

  # 3. Compara a string tratada com a string invertida
  return frase_tratada == frase_invertida

# Exemplos de uso:
print(f"'arara' é palíndromo? {eh_palindromo('arara')}")
print(f"'A diva em breve vê a vida' é palíndromo? {eh_palindromo('A diva em breve vê a vida')}")
print(f"'O lobo' é palíndromo? {eh_palindromo('O lobo')}")
print(f"'Hello' é palíndromo? {eh_palindromo('Hello')}")
