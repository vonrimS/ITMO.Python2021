from random import randint
import time

gambler1 = input ('Введите имя 1го игрока: ')
gambler2 = input ('Введите имя 2го игрока: ')

total1 = 0
total2 = 0

def throw_dice(gambler, total):
    print('...кубик бросает', gambler)
    time.sleep(2)
    n = randint(1, 6)
    print('Выпало', n)
    total += n
    # print(f'Итоговый результата игрока {gambler} : {total}')
    return total

# три хода у каждого игрока
for turn in range(3):
    total1 = throw_dice(gambler1, total1)
    total2 = throw_dice(gambler2, total2)

# подводим итоги по результатам набранных очков
def get_winner (score1, score2):
    print(f'{score1} : {score2}')
    if score1 > score2:
        print(f'игрок {gambler1} победил!!!')
    elif score1 < score2:
        print(f'игрок {gambler2} победил!!!')
    else:
        print('...ничья')


get_winner(total1, total2)