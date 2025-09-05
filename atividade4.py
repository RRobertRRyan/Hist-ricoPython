#Crie uma função chamada mostrar_tabuada que receba um número inteiro como parâmetro. A função deve imprimir a tabuada de multiplicação desse número, do 1 ao 10, no formato "numero x i = resultado".#

def mostrar_tabuada(numero):
    """
    Imprime a tabuada de multiplicação de um número, de 1 a 10.

    Args:
      numero: O número inteiro para o qual a tabuada será gerada.
    """
    print(f"Tabuada de {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")


mostrar_tabuada(5)
