from random import choice


first = 'Мама мыла раму'
second = 'Рамена мало было'

resultat = map(lambda x,y: x==y, first, second)
print(list(resultat))

# Напишите функцию get_advanced_writer(file_name), принимающую название файла для записи.
# Внутри этой функции, напишите ещё одну - write_everything(*data_set), где *data_set - параметр
# принимающий неограниченное количество данных любого типа.
# Логика write_everything заключается в добавлении в файл file_name всех данных из data_set в том же виде.
# Функция get_advanced_writer возвращает функцию write_everything.


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w', encoding='utf-8') as file:
            for i in data_set:
                file.write(f'{i}\n')
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# Метод __call__:
# Создайте класс MysticBall, объекты которого обладают атрибутом words хранящий коллекцию строк.
# В этом классе также определите метод __call__ который будет случайным образом выбирать слово
# из words и возвращать его. Для случайного выбора с одинаковой вероятностью для каждого данного
# в коллекции можете использовать функцию choice из модуля random.

class MysticBall:
    def __init__(self,*words):
        self.words = words
    def __call__(self):
        return choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
