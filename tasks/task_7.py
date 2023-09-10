# Пользовательский ввод данных
number: int = int(input("Введите целое число: "))
number_2: float = float(input("Введите дробное число: "))
string: str = input("Введите строку: ")

if number:
    if number_2:
        if string:
            print("Да")
    else:
        print("Нет")
