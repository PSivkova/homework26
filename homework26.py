# Создайте минимум два своих собственных исключения, наследуя их от класса Exception
# Например, InvalidDataException и ProcessingException.
# Напишите функцию, которая генерирует различные исключения в зависимости от передаваемых ей аргументов.
# Добавьте обработку исключений в функции, вызывающие вашу функцию, и передайте исключения дальше по стеку вызовов.
# В основной части программы вызовите эти функции и корректно обработайте

class DivisionError(Exception):
    pass


class ProZero(Exception):
    pass


def division(a, b):
    try:
        if a < b:
            raise DivisionError('Нельзя делить меньшее на большее')
        if b == 0:
            raise ProZero('Нельзя делить на ноль')
    except (DivisionError, ProZero) as exc:
        print(f'Поймано моё исключение: {exc}')
    else:
        print(f"Успех, {a/b}")


division(3, 5)
division(3, 0)
division(8, 2)

