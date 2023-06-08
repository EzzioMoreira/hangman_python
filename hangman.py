from utils import show_difficult_menu
from utils import select_word
from utils import play_hangman

if __name__ == '__main__':
    difficulty_setting = show_difficult_menu()
    select_word = select_word(difficulty_setting)
    
    play_winner = play_hangman(select_word, difficulty_setting)
    if play_winner:
        print(f'\nParabéns, você ganhou 😃🥳!\n')
    else: 
        print(f'\nQue pena, você perdeu 😮‍💨!\n')
    print(f'\nA palavra escolhida: {select_word} 🤯.\n')
