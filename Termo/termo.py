import random
import pyfiglet

hello = pyfiglet.figlet_format("Termo!")
print(hello)
print('Write a FIVE letters word, the colors will show you whats WRONG or RIGHT:')
print('π© Have this letter in the word, and the position is right.')
print('π¨ Have this letter in the word, but the position is wrong.')
print('β¬οΈDont have this letter in the word!')
print()

words = ['vigor', 'brado', 'causa', 'sonho', 'tempo', 'anexo', 'moral', 'assim', 'nobre', 'algoz', 'senso', 'mexer', 'sagaz']
random_word = random.choice(words).upper()

code_word = ["β¬οΈ", "β¬οΈ", "β¬οΈ", "β¬οΈ", "β¬οΈ"]

life = 6
win_check = 0
pos_guessed = 0

while life != 0 and win_check != 5:
    win_check = 0

    guessed_word = input(f"{life}. Guess your five letter word: ").upper()
    guessed_word_list = []
    for caractere in guessed_word:
        guessed_word_list += caractere

    if len(guessed_word) == 5:
        for letter in guessed_word_list:
            if letter in random_word and letter != random_word[pos_guessed]:
                code_word[pos_guessed] = 'π¨'
            elif letter in random_word and letter == random_word[pos_guessed]:
                code_word[pos_guessed] = 'π©'
                win_check += 1
            else:
                code_word[pos_guessed] = 'β¬οΈ'

            pos_guessed += 1

            if pos_guessed > 4:
                code_word_str = ''
                for square in code_word:
                    code_word_str += str(square)

                print(code_word_str, '\n')
                pos_guessed = 0
                life -= 1

    if len(guessed_word) != 5:
        print('\n ( π£ Please, write a five letters word! π£ ) \n')
        life -= 1



if life == 0 or win_check == 5:
    if life == 0 and win_check != 5:
        print(f'π€ You lose! The word is "{random_word}"! π€')
    elif life == 0 and win_check == 5:
        print(f'βπ You win! The word is "{random_word}"! βπ')
    elif life != 0 and win_check == 5:
        print(f'βπ You win! The word is "{random_word}"! βπ')
    play_again = input('Thanks for playing!')

