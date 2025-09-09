
# A senha correta definida pelo programa
senha_correta = "python123"

# Variável para armazenar o que o usuário digita
senha_digitada = ""

# O laço 'while' continua enquanto a senha estiver incorreta
while senha_digitada != senha_correta:
  senha_digitada = input("Digite a senha para ter acesso: ")

# Quando o laço termina, significa que a senha está correta
print("Acesso concedido.")

