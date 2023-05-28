# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также может
# ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных

import os
import re

path_file = 'tel_book.txt'


def read_file():
    if not os.path.isfile(path_file):
        print('Файл пуст.')
    else:
        with open(path_file, 'r', encoding='UTF-8') as f:
            for line in f:
                print(line.strip())



def find_file():
    find_info = input('Введите значение поля, которое нужно найти: ')
    with open(path_file, 'r', encoding='UTF-8') as f:
        for line in f:
            if find_info.casefold() in line.casefold():
                print(line.strip())


def add_user():
    surname = input("Введите фамилию: ")
    name = input("Введите имя: ")
    patronymic = input("Введите отчество: ")
    phone = input("Введите номер телефона в формате +7xxxxxxxxxx: ")
    if not re.match(r'^\+7\d{10}$', phone):
        print("Некорректный формат номера телефона. Введите номер в формате +7xxxxxxxxxx")
        return
    record = f"{surname} {name} {patronymic} {phone}"
    with open(path_file, 'a', encoding='UTF-8') as f:
        f.writelines('\n' + record)
    print("Запись успешно добавлена в справочник")


def delete_user():
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    with open(path_file, 'r', encoding='UTF-8') as f:
        lines = f.readlines()
    with open(path_file, 'w', encoding='UTF-8') as f:
        found = False
        for line in lines:
            fields = line.strip().split()
            if fields[0] == last_name and fields[1] == first_name:
                found = True
            else:
                f.write(line)
        if not found:
            print('Пользователь не найден.')
        else:
            print('Запись успешно удалена.')


def modify_user():
    last_name = input('Введите фамилию пользователя, данные которого нужно изменить: ')
    first_name = input('Введите имя пользователя, данные которого нужно изменить: ')
    with open(path_file, 'r', encoding='UTF-8') as f:
        lines = f.readlines()
    with open(path_file, 'w', encoding='UTF-8') as f:
        found = False
        for line in lines:
            fields = line.strip().split()
            if fields[0] == last_name and fields[1] == first_name:
                found = True
                while True:
                    print('\nВыберите поле, которое нужно изменить:\n'
                        ' - Фамилия: 1\n'
                        ' - Имя: 2\n'
                        ' - Отчество: 3\n'
                        ' - Телефон: 4\n'
                        ' - Выйти из режима редактирования: 5')
                    field = input('Выберите поле: ')
                    if field == '1':
                        new_last_name = input('Введите новую фамилию: ')
                        fields[0] = new_last_name
                    elif field == '2':
                        new_first_name = input('Введите новое имя: ')
                        fields[1] = new_first_name
                    elif field == '3':
                        new_patronymic = input('Введите новое отчество: ')
                        fields[2] = new_patronymic
                    elif field == '4':
                        new_phone = input('Введите новый номер телефона в формате +7xxxxxxxxxx: ')
                        if not re.match(r'^\+7\d{10}$', new_phone):
                            print("Некорректный формат номера телефона. Введите номер в формате +7xxxxxxxxxx")
                            continue
                        fields[3] = new_phone
                    elif field == '5':
                        break
                    else:
                        print('Неверный ввод. Попробуйте еще раз.')
                line = ' '.join(fields) + '\n'
            f.write(line)
        if not found:
            print('Пользователь не найден.')
        else:
            print('Запись успешно изменена.')

def main():
    while True:
        print('\nКоманды для работы со справочником:\n'
            ' - Просмотр всех записей справочника: 1\n'
            ' - Поиск по справочнику: 2\n'
            ' - Добавление новой записи: 3\n'
            ' - Удаление записи из справочника по Имени и Фамилии: 4\n'
            ' - Изменение любого поля в определенной записи справочника: 5\n'
            ' - Выход: 6')
        action = input('Выберите действие: ')
        if action == '1':
            read_file()
        elif action == '2':
            find_file()
        elif action == '3':
            add_user()
        elif action == '4':
            delete_user()
        elif action == '5':
            modify_user()
        elif action == '6':
            break
        else:
            print('Неверный ввод. Попробуйте еще раз.')


if name == 'main':
    main()
