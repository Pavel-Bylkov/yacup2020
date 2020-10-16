# coding: utf-8

TICKET_LOGS = 'ticket_logs.csv'

LETTERS_TO_NUMBERS_DICT = {
    'a': 2, 'b': 2, 'c': 2, 'd': 3, 'e': 3, 'f': 3, 'g': 4, 'h': 4, 'i': 4, 'j': 5, 'k': 5, 'l': 5, 'm': 6, 'n': 6,
    'o': 6, 'p': 7, 'q': 7, 'r': 7, 's': 7, 't': 8, 'u': 8, 'v': 8, 'w': 9, 'x': 9, 'y': 9, 'z': 9,
}


def read_input_data():
    """
    Возвращает строки файла с данными TICKET_LOGS, разбивая их на столбцы с названием спектакля и номером телефона.
    Пример:
    logs = read_input_data()
    print(logs[:3])

    Результат:
    [['Кошки', '+88029264576'], ['Норма', '8805-630-71-19'], ['Евгений Онегин', '8-(802)-235-30-28']]

    :return: list
    """
    with open(TICKET_LOGS) as f:
        return [line.strip().split(',') for line in f]


def remove_hyphens_and_parenthesis(logs):
    """
    Возвращает список спектаклей и телефонов logs, в телефонах которых удалены скобки и дефисы.
    Пример:
    logs = [['Кошки', '+88029264576'], ['Норма', '8805-630-71-19'], ['Евгений Онегин', '8-(802)-235-30-28']]
    logs_formatted = remove_hyphens_and_parenthesis(logs)
    print(logs_formatted[:3])

    Результат:
    [['Кошки', '+88029264576'], ['Норма', '88056307119'], ['Евгений Онегин', '88022353028']]

    :param logs: list список списков строк (результат функции read_input_data)
    :return: list
    """
    return [[rec[0], rec[1].replace('(', '').replace(')', '').replace('-', '')] for rec in logs]


def remove_plus_sign(logs):
    """
    Возвращает список спектаклей и телефонов logs, в телефонах которых удалены плюсы.
    Пример:
    logs = [['Кошки', '+88029264576'], ['Норма', '88056307119'], ['Евгений Онегин', '88022353028']]
    logs_formatted = remove_plus_sign(logs)
    print(logs_formatted[:3])

    Результат:
    [['Кошки', '88029264576'], ['Норма', '88056307119'], ['Евгений Онегин', '88022353028']]

    :param logs: list список списков строк
    :return: list
    """
    return [[rec[0], rec[1].replace('+', '')] for rec in logs]


def translate_letters_to_numbers(phone):
    """
    Возвращает номер телефона, в котором буквы заменены на соответствующие цифры.
    Используется стандартная раскладка букв алфавит на клавиатуре телефона.

    Пример:
    translate_letters_to_numbers('8803tonight')

    Результат:
    '88038664448'

    :param phone: str номер телефона с цифрами и буквами
    :return: str
    """
    digits_list = [letter if letter.isnumeric() else LETTERS_TO_NUMBERS_DICT[letter] for letter in phone]
    return ''.join([str(d) for d in digits_list])


def convert_letters(logs):
    """
    Возвращает список спектаклей и телефонов logs, в телефонах которых буквы заменены на соответствующие цифры.
    Используется стандартная раскладка букв алфавит на клавиатуре телефона.
    Пример:
    logs = [['Ночь перед Рождеством', '8803tonight'], ['Норма', '8806dollars'], ['Евгений Онегин', '8804weapons']]
    print(convert_letters(logs))

    Результат:
    [['Ночь перед Рождеством', '88038664448'], ['Норма', '88063655277'], ['Евгений Онегин', '88049327667']]

    :param logs: list список списков строк
    :return: list
    """
    return [[rec[0], translate_letters_to_numbers(rec[1])] for rec in logs]


def build_performances_dict(logs):
    """
    Возвращает словарь спектаклей со списком номеров телефонов для каждого.
    Данные берутся из файла FORMATTED_FILE_LOCATION. Пример результата:

    {
        'Евгений Онегин': ['88014347948', '88038998203', ...],
        'Вестсайдская история': ['88026153027', '88076313455', ...],
        ...
    }

    :return: dict
    """
    performances_dict = {}

    for line in logs:
        performance, phone = line
        performances_dict.setdefault(performance, [])
        performances_dict[performance].append(phone)

    return performances_dict


def unique_phones_calculation(performances_dict):
    """Возвращает словарь с числом уникальных телефонных номеров"""
    return {performance: len(set(phones)) for performance, phones in performances_dict.items()}


def main():
    logs = read_input_data()

    # удаляем очевидные лишние символы: скобки и дефис
    logs_formatted = remove_hyphens_and_parenthesis(logs)

    # проверим есть ли телефоны, длина которых отлична от 11 (например, в первой строке точно такой номер)
    not_11_digit_phones = [rec[1] for rec in logs_formatted if len(rec[1]) != 11]
    print('Не одиннадцатизначные номера (первые 5 штук):', not_11_digit_phones[:5])

    logs_formatted = remove_plus_sign(logs_formatted)

    # проверим остались ли теперь телефоны, длина которых отлична от 11
    not_11_digit_phones = [rec[1] for rec in logs_formatted if len(rec[1]) != 11]
    print('Есть не одиннадцатизначные номера!' if not_11_digit_phones else 'Все номера из 11 цифр ура')

    # Проверим остались ли номера, состоящие не только из цифр (в первом варианте not_11_digit_phones такие попадались)
    not_digit_phones = [rec[1] for rec in logs_formatted if not rec[1].isnumeric()]
    print('Номера, содержащие не только цифры (первые 5 штук):', not_digit_phones[:5])

    logs_formatted = convert_letters(logs_formatted)

    performances_dict = build_performances_dict(logs_formatted)
    stats = unique_phones_calculation(performances_dict)

    print(sorted(stats.items(), key=lambda x: -x[1]))


if __name__ == '__main__':
    main()
