year: int = int(input("Введите год: "))
month: int = int(input("Введите месяц: "))

month_nums: list = [1, 3, 5, 7, 8, 10, 12]

is_leap_year: bool = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

if is_leap_year and month in month_nums:
    print("Да")
else:
    print("Нет")
