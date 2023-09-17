# Пользовательский ввод данных
number: int = int(input("Введите целое число: "))
number_2: float = float(input("Введите дробное число: "))
string: str = input("Введите строку: ")
proverka = (number, number_2, string)
# Topic 5
# Встроенные функции Python: для работы с коллекциями и числами

if all(proverka):
    print("Да")
else:
    print("Нет")
