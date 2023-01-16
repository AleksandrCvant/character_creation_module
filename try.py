from math import sqrt

message: str = ('Добро пожаловать в самую '
                'лучшую программу, для вычисления '
                'квадратного корня из заданного числа')


def calculate_square_root(number: float) -> float:
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number: float) -> None:
    """Проверка верности выражения."""
    if your_number <= 0:
        return print('Не математично!')
    elif your_number > 0:
        root = calculate_square_root(your_number)
        return print(f'Мы вычислили квадратный корень из введённого вами числа. '
          f'Это будет: {root}')


print(message)
calc(25.5)
