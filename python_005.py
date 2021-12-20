from random import randint
import time

def state_player():
    return {"name": input('Введите имя игрока: '), "score": 0}

def get_name(person):
    return (person["name"])

def get_score(person):
    return (person["score"])

def now_rolling (person):
    print('...кубик бросает', get_name(person))
    time.sleep(2)
    n = randint(1, 6)
    print('Выпало', n)
    person["score"] += n
    # print(f'Итоговый результат игрока {get_name(person)} : {get_score(person)}')

def roll_the_dice(person1, person2):
    roll_qnt = int(input('Сколько бросков будут делать игроки? '))
    for roll in range(roll_qnt):
        now_rolling(person1)
        now_rolling(person2)

# подводим итоги по результатам набранных очков
def get_winner (person1, person2):
    score1 = get_score(person1)
    score2 = get_score(person2)
    print(f'{score1} : {score2}')
    if score1 > score2:
        print(f'игрок {get_name(person1)} победил!!!')
    elif score1 < score2:
        print(f'игрок {get_name(person2)} победил!!!')
    else:
        print('...ничья')


