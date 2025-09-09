
# Inicializa a variável para armazenar a soma
soma_total = 0

# Pede o primeiro número ao usuário
numero = int(input("Digite um número (digite 0 para encerrar): "))

# O laço 'while' continua enquanto o número digitado for diferente de 0
while numero != 0:
  # Adiciona o número digitado à soma total
  soma_total += numero
  
  # Pede o próximo número, para a próxima iteração do laço
  numero = int(input("Digite outro número (0 para encerrar): "))

# O laço termina e a soma final é exibida
print(f"A soma total dos números digitados é: {soma_total}")
