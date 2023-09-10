year: int = int(input("Введите год: "))
month: int = int(input("Введите месяц: "))

month_nums = ...

is_leap_year: bool = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
