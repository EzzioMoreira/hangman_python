import random
from constants import DIFFICULT_LEVELS, WORDS_LENGTHS
import re

def show_difficult_menu():
    '''
    Exibe o menu de dificuldade e retorna a dificuldade escolhida pelo usuário.

    :return: Uma string que representa o nível de dificuldade escolhido pelo usuário.
    '''
    print(f'\nA seguir escolha um nível de dificuldade:\n')
    difficult_setting = ''
    
    '''
    While para validar a entrada do usuário, caso o usuário digite um valor que não esteja no dicionario difficult_levels, o programa vai pedir para digitar novamente.
    '''
    while not difficult_setting:
        for key, value in DIFFICULT_LEVELS.items():
            print(f'{key} - {value.upper()}')
        
        difficult_setting = input(f'\nDigite o número correspondente ao nível de dificuldade: ')
    
        if difficult_setting not in DIFFICULT_LEVELS.keys():
            print(f'{DIFFICULT_LEVELS}, nao é uma opçao valida...')
            difficult_setting = ''
    
    return difficult_setting

def select_word(difficult_setting):
    '''
    Abre o arquivo words.txt e retorna uma palavra aleatória de acordo com o nível de dificuldade escolhido pelo usuário.

    :param difficult_setting: Uma string que representa o nível de dificuldade escolhido pelo usuário.
    :return: Uma string que representa a palavra escolhida pelo usuário.
    '''
    ''' 
    - With função python, gerenciador de contexto, python acegura que vai abrir o arquivo e fechar o arquivo.
    - Isso evita problemas de processamento, como o arquivo ficar aberto e não conseguir abrir novamente.
    - Evita fazamento de memória.
    '''
    with open('static/words.txt', mode='r') as f_words:
        # lista vazia para armazenar as palavras
        words = []
        for i in f_words.readlines():
            # strip remove os espaços em branco
            w = i.strip()
            # min, max indexando o dicionario words_lengths, com a chave difficult_setting
            min, max = WORDS_LENGTHS[difficult_setting]
            # len retorna o tamanho da palavra, se o tamanho da palavra for maior que o minimo e menor que o maximo, adiciona a palavra na lista words.
            if len(w) >= min and len(w) <= max:
                words.append(w)
    
    # max_index recebe o tamanho da lista words -1, pois o index começa em 0.
    max_index = len(words) -1
    # random.randint retorna um numero aleatorio entre 0 e o max_index
    radom_index = random.randint(0, max_index)
    # select_word recebe a palavra da lista words, no index radom_index
    select_word = words[radom_index]
    
    return select_word

def select_total_tries(select_word, difficult_setting):
    '''
    Total de chances que o usuário terá para acertar a palavra.

    :param select_word: Uma string que representa a palavra escolhida pelo usuário.
    :param difficult_setting: Uma string que representa o nível de dificuldade escolhido pelo usuário.
    :return: Uma string que representa a palavra escolhida pelo usuário.
    '''
    # set retorna os caracteres unicos da palavra
    unique_letters = set(select_word)
    
    # total_tries recebe o tamanho da palavra * 2
    total_tries = 1.5 * len(unique_letters)
    
    if difficult_setting == '1':
        total_tries += 2
    elif difficult_setting == '3':
        total_tries -= 2
        # min retorna o menor valor entre os dois valores
        total_tries = min([total_tries, 18])
    
    # round arredonda o numero para o valor mais próximo do float
    total_tries = round(total_tries)

    return total_tries

def play_hangman(select_word, difficulty_setting):
    '''
    Função principal do jogo, onde o usuário vai tentar acertar a palavra escolhida.

    :param select_word: Uma string que representa a palavra escolhida pelo usuário.
    :defficulty_setting: Uma string que representa o nível de dificuldade escolhido pelo usuário.
    '''
    total_tries = available_tries = select_total_tries(select_word, difficulty_setting)
    current_state = ['_' for letter in select_word]
    guessed_letters = []

    while '_' in current_state and available_tries:
        print(f'\n\n#### Tentativa número: {total_tries - available_tries + 1} de {total_tries} ####')
        for i in current_state:
            print(i, end=' ')
        
        # 1 - guess não é vazia,
        # 2 - guess não é uma letra.
        # 3 - contém apenas uma letra.
        guess = ''
        while not guess:
            guess = input('\nDigite uma letra: ').lower()
            if len(guess) != 1 or not re.match('[a-z]', guess):
                print('Entrada inválida, tente novamente. Digite apenas uma letra.')
                guess = ''
        
        if guess not in guessed_letters:
            guessed_letters.append(guess)
    
            if guess in select_word:
                pass
                positions = [letter.start() for letter in re.finditer(guess, select_word)]
                for index in positions:
                    current_state[index] = guess
            else:
                available_tries -= 1
        else:
            print(f'Você já tentou a letra {guess}, tente outra.')

    return available_tries