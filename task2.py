# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""


import os
import random
import shutil

def is_positive(num: str) -> bool:
    return num.isdigit() and num != '0'


def candy_bot(bank: int, move: int, level: str) -> int:
    if level == '1':
        result = random.randint(1, move) if bank > move else bank
    elif level == '2':
        if bank > move and not (bank // (move + 1)) % 5: result = random.randint(1, move)
        else: result = bank % (move + 1) if bank % (move + 1) else random.randint(1, move)
    elif level == '3':
        result = bank % (move + 1) if bank % (move + 1) else random.randint(1, move)
    return result

def welcome() -> None:
    os.system('cls')
    width = shutil.get_terminal_size().columns
    print('Вас приветствует игра "Сладкоешка"!\n'.center(width))
    rules = ('| - На столе лежит куча конфета.', 
            '| - За один ход можно забрать заранее определенное количество конфет.', 
            '| - Играют два игрока делая ход друг после друга.', 
            '| - Первый ход определяется жеребьёвкой.', 
            '| - Все конфеты оппонента достаются сделавшему последний ход.')          
    pos = (width - max(map(len, rules))) // 2
    print('Правила игры просты:\n'.rjust(width - pos))
    for line in rules: 
        print(' ' * pos, line, ' ' * (width - 2 * pos - len(line)), '|', sep='')
    print()
    print('Нажмите Enter для продолжения!'.center(width))
    input()

def candy_game(bank: int, max_move: int) -> None:
    os.system('cls')
    default = str(bank)
    while default:
        bank = int(default)
        bank_text = (f'\n На столе\033[33m\033[1m {bank} \033[0mконфет.\n'
                ' Введите\033[33m\033[3m новое значение \033[0mили нажмите\033[34m Enter \033[0mдля продолжения: ')
        while not (is_positive(default := input(bank_text)) or default == ''):
            print('\n\033[31m Количество конфет должно быть положительным числом!! \033[0m')    
    default = str(max_move)
    while default:
        max_move = int(default)
        move_text = (f'\n За ход можно забрать не более\033[33m\033[1m {max_move} \033[0mконфет.\n'
                ' Введите\033[33m\033[3m новое значение \033[0mили нажмите\033[34m Enter \033[0mдля продолжения: ')
        while not (is_positive(default := input(move_text)) and int(default) < bank // 5 or default == ''):
            print('\n\033[31m Размер хода должен быть минимум в пять раз меньше, чем количество конфет на столе!! \033[0m')
    os.system('cls')    
    player_1 = input(' Введите имя игрока: \033[32m')
    player_2 = input('\033[0m Для игры \033[32m"Игрок против игрока"\033[0m введите имя второго игрока. '
                     ' Для игры \033[32m"Игрок против бота"\033[m нажмите\033[34m Enter\033[0m: \033[32m')
    if player_2 == '': 
        player_2 = 'Бот-Сладкоежка'
        level_text = ('\n\033[0m 1 - бот равнодущен к сладкому. \n' 
                      ' 2 - бот любит конфеты! \n' 
                      ' 3 - бот безумный фанат конфет!! \n'
                      ' Введите уровень сложности: ')
        while (level := input(level_text)) not in ('1', '2', '3'):
            print('\n\033[31m Введите 1, 2 или 3! \033[0m')
    input('\n Нажмите\033[34m Enter \033[0mчто бы случай определил кто ходит первым!\n И игра начнется!!')   
    os.system('cls')
    turn = random.randint(0, 1)
    while bank > 0:
        player = player_1 if turn else player_2
        game_text = f'\n\033[0m На столе\033[33m\033[1m {bank} \033[0mконфет!\n Ходит\033[32m {player}: \033[0m\033[33m'
        if player == 'Бот-Сладкоежка':
            move = candy_bot(bank, max_move, level)
            print(game_text, move, sep = '')
        else:
            while not is_positive(move := input(game_text)) or int(move) > max_move:
                print(f'\n\033[31m За ход можно взять от 1 до {max_move} конфет! \033[0m')
        bank -= int(move)
        turn = not turn
    print(f'\n\033[0m\033[33m Все конфеты достаются:\033[32m\033[1m {player} \033[0m \n')
    
def main():
    welcome()
    candy_game(2021, 28)


if __name__ == '__main__':
    main()


