#Crie uma função chamada verificar_idade que receba um número inteiro (a idade) como parâmetro. A função deve imprimir "Você é maior de idade." se a idade for maior ou igual a 18, e "Você é menor de idade." caso contrário, faça e me explique em python.#

def verificar_idade(idade):
    """
    Verifica se uma pessoa é maior ou menor d eidade com base na idade fornecida.

    Args:
     idade: Um número inteiro representado a idade da pessoa. 
    """
    if idade >= 18:
        print("Você é maior de idade.")
    else: 
        print("Você é maior d eidade.")

verificar_idade(25)
verificar_idade(17)
verificar_idade(18)
