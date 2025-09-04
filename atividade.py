
def contar_vogais(texto):
  # Transforma a string em minúsculas para contar vogais maiúsculas e minúsculas.
  texto = texto.lower()
  contador = 0
  for letra in texto:
    if letra in 'aeiou':
      contador += 1
  return contador

# Exemplo de uso:
frase = "Olá, mundo!"
total_vogais = contar_vogais(frase)
print(f"O número de vogais é: {total_vogais}")