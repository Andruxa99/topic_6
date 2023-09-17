year: int = int(input("Введите год: "))
month: int = int(input("Введите месяц: "))

month_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

is_leap_year: bool = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

if ...:
    print("Да")
else:
    print("Нет")
