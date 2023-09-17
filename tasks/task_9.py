#  Пользовательский ввод
number: int = int(input("Введите целое число: "))
number_2: float = float(input("Введите дробное число: "))
string: str = input("Введите строку: ")

data: tuple = (number, number_2, string)

if any(data):
    print("Да")
else:
    print("Нет")
