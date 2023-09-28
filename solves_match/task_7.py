number: int = int(input("Введите целое число: "))
number_2: float = float(input("Введите дробное число: "))
string: str = input("Введите строку: ")

data: tuple = (number, number_2, string)

match all(data):
    case True:
        print("Да")
    case _:
        print("Нет")
