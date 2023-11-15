import random

palavra = ['python', 'programação', 'HTML', 'CSS', 'Angular']


def seleciona_palavra():
    """
    Função responsável por sortear palavra
    :return: Palavra sorteada
    """
    posicao = random.randrange(0, len(palavra))

    return palavra[posicao]




