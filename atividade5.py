#Jogo de Adivinhação#

numero_secreto = 42

palpite = int(input("Tente adivinhar o número secreto: "))

while palpite != numero_secreto:
    if palpite > numero_secreto:
        print("O número secreto é menor. Tente novamente.")
    else:
        print("O número secreto é maior. Tente novamente.")

    palpite = int(input("Qual o seu próximo palpite? "))

print("Parabéns você ecertou.")