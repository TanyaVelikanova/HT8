# Модуль для ввода/вывода информации


def choose() -> str:
    """"Выбор режима работы приложения"""
    result = input('Выберите режим, 1 - задачи, 2 - уравнения, 3 - многочлены, 4 - история: ')
    return result


def get_expr() -> str:
    """"Запрашивает у пользователя задачу"""
    expr = input('Введите выражение для вычисления: ') 
    return expr


def show_res(expr: str, res: str):
    """Выводит результат"""
    print(f'{expr} = {res}')


def erorr_mode():
    """Выводит сообщение об ошибке выбора режима"""
    print('Выберите режим 1-4')



def show_history(history: str):
    """Выводит истроию оперций"""
    print('\n'.join(history))

