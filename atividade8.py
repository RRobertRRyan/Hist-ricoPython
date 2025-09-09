
# Solução 1: Usando um laço for (mais didática)
def inverter_string_com_laco(texto):
  """
  Inverte uma string usando um laço for e a retorna.
  """
  string_invertida = ""
  for caractere in texto:
    string_invertida = caractere + string_invertida
  return string_invertida

# Solução 2: Usando o fatiamento de string (mais "pythônica")
def inverter_string_com_fatiamento(texto):
  """
  Inverte uma string usando fatiamento [::-1] e a retorna.
  """
  return texto[::-1]

# Exemplos de uso para ambas as funções:
texto_original = "python"

print(f"Texto original: {texto_original}")

# Usando a primeira solução
invertida1 = inverter_string_com_laco(texto_original)
print(f"Invertida (com laço): {invertida1}")

# Usando a segunda solução
invertida2 = inverter_string_com_fatiamento(texto_original)
print(f"Invertida (com fatiamento): {invertida2}")
