# Пользовательский ввод данных
number: int = int(input("Введите целое число: "))
number_2: float = float(input("Введите дробное число: "))
string: str = input("Введите строку: ")

data: tuple = (number, number_2, string)

if all(data):
    print("Да")
else:
    print("Нет")
