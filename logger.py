# Модуль для записи резуьтатов вычислений

def log_exec(expr: str, result: str):
    """Записывает в файл результат вычислений
    в виде |задача -> ответ|"""
    with open('log.txt', 'a') as f:
        f.write(f'{expr} = {result}\n')


def get_history() -> str:
    """"Возвращает содержимое файла с результатами вычислений"""
    with open('log.txt', 'r') as f:
        result = f.read().split('\n')
        return result