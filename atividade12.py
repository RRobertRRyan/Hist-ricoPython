
def contar_palavras(frase):
    """
    conta o número de palavras em ma string.

    Args: 
    frase: A string (frase) a ser analisada.

    Returns: 
    O número de palavras na frase.

    """

    frase = frase.strip()

    if not frase:
        return 0
    palavras = frase.split()

    return len(palavras)

frase1 = "Olá mundo!"
print(f"A frase {frase1} tem {contar_palavras(frase1)} palavras.")

frase1 = "Isso é um teste."
print(f"A frase {frase1} tem {contar_palavras(frase1)} palavras.")

frase1 = "Isso é apenas uma frase."
print(f"A frase {frase1} tem {contar_palavras(frase1)} palavras.")

