'''
Constante, (variavel) do tipo dicionario, onde a chave é o numero do nivel de dificuldade e o valor é o nome do nivel de dificuldade.
Por conversão de código, o nome da variavel é em maiusculo.
'''
DIFFICULT_LEVELS = {
    '1': 'facil',
    '2': 'normal',
    '3': 'dificil',
}

'''
Variavel do tipo dicionario, onde a chave é o numero do nivel de dificuldade e o valor é uma tupla com o tamanho minimo e maximo da palavra.
'''
WORDS_LENGTHS = {
    '1': (3, 5),
    '2': (6, 10),
    '3': (10, 10000),
}
