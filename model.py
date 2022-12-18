# Модуль для выполнения опреаций

import sympy

def execute_expr(expr: str) -> str:         # (5+3)*10 -> 80
    """"Принимает на вход строку-пример.
    Возвращает результат примера."""
    result = eval(expr)
    return result


def solve_eq(expr: str) -> str:                    # x**3 - 8 = 0 -> "2"
                                                    # x**2 - 1 = 0 -> "1,-1"
    """Принимает на вход уравнение в виде строки.
    Возвращает список корней уравнения в строку с разделителем"""
    x = sympy.Symbol('x')
    result_s = sympy.solve(expr, x)
    result_s= [str(i) for i in result_s]
    result = ','.join(result_s)
    return result
    

def simpify_pol(expr: str) -> str:           # x**2 + 3*x**2 + 4 -> 4*x**2 + 4
    """"Упрощает введенный многочлен"""
    x = sympy.Symbol('x')
    result = str(sympy.simplify(expr))
    return result
