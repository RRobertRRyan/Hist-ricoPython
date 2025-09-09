
# Reutilizando as funções dos exercícios anteriores

def contar_vogais(texto):
  """Conta o número de vogais em uma string."""
  vogais = "aeiouAEIOU"
  contador = 0
  for caractere in texto:
    if caractere in vogais:
      contador += 1
  return contador

def inverter_string(texto):
  """Inverte uma string usando fatiamento."""
  return texto[::-1]

# --- Programa Principal ---

while True:
  # Exibe o menu de opções
  print("\n--- Menu ---")
  print("1. Contar vogais de uma palavra")
  print("2. Inverter uma palavra")
  print("3. Sair")
  
  # Solicita a opção do usuário
  opcao = input("Escolha uma opção: ")

  # Lógica para cada opção
  if opcao == '1':
    palavra = input("Digite a palavra: ")
    num_vogais = contar_vogais(palavra)
    print(f"A palavra '{palavra}' tem {num_vogais} vogais.")
  
  elif opcao == '2':
    palavra = input("Digite a palavra: ")
    palavra_invertida = inverter_string(palavra)
    print(f"A palavra invertida é: {palavra_invertida}")
  
  elif opcao == '3':
    print("Saindo do programa. Até logo!")
    break  # Encerra o laço 'while'
  
  else:
    print("Opção inválida. Por favor, escolha 1, 2 ou 3.")
