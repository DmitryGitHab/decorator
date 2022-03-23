# https://replit.com/@chigiwar/decor#main.py
import datetime


def logger(path):
    def decorator(foo):
        def new_foo(*args, **kwargs):
            time_now = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
            result = foo(*args, **kwargs)
            loggs = f'''
Вызвана функция: {foo.__name__}
Время вызова функции: {time_now}
Аргументы функции: {args}, {kwargs}
Результат функции: {result}\n '''
            with open(path, 'w', encoding='UTF-8') as f:
                f.write(loggs)
            return result
        return new_foo
    return decorator


@logger(path='loggs.txt')
def test_function():
    print('Выполнение какой-то тестовой функции')

test_function()


"""далее применение декоратора на одном из прошлых ДЗ """

import requests
TOKEN = "2619421814940190"

class SuperHero():
    def __init__(self, name):
        self.name = name
        self.id = get_id(self.name)
        self.intelligence = int(get_intelligence(self.id))

    def __str__(self):
        return f'{self.name} id: {self.id}, обладает интеллектом: {self.intelligence}'

    def __lt__(self, other):
        return self.intelligence > other.intelligence

@logger(path='loggs.txt')
def get_id(name):
    url = f'https://www.superheroapi.com/api.php/{TOKEN}/search/{name}'
    response = requests.get(url)
    id = response.json()
    check_box = 0  # переменная для отслеживания совпадения имени персонажа
    for i in id['results']:
        if name == i['name']:
            check_box_found = check_box  # присваивание индекса найденного персонажа
        check_box += 1
    print('id искомого персонажа: ', id['results'][check_box_found]['id'])
    return id['results'][check_box_found]['id']

get_id('Thanos')