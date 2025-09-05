
def contar_vogais(texto):
  """
  Conta o número de vogais (a, e, i, o, u) em uma string.

  Args:
    texto: A string a ser analisada.

  Returns:
    O número total de vogais na string.
  """
  # As linhas abaixo estão identadas para dentro da função.
  vogais = "aeiouAEIOU"
  contador = 0
  for caractere in texto:
    if caractere in vogais:
      contador += 1
  return contador

# Exemplos de uso da função:
frase1 = "Hello World"
print(f"O número de vogais em '{frase1}' é: {contar_vogais(frase1)}")

frase2 = "Python é incrível"
print(f"O número de vogais em '{frase2}' é: {contar_vogais(frase2)}")

frase3 = "RYTHM"
print(f"O número de vogais em '{frase3}' é: {contar_vogais(frase3)}")
