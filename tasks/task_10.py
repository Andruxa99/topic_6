ALPHABETS = {
    "en_vowels": "AEIOU",
    "en_consonants": "BCDFGHJKLMNPQRSTVWXYZ",
    "ru_vowels": "АЕЁИОУЫЭЮЯ",
    "ru_consonants": "БВГДЖЗЙКЛМНПРСТФХЦЧШЩЪЬ",
}

print("Добро пожаловать в программу \"Буква-Детектив\"!", end="\n\n")

print("Выберите алфавит:""\n"
      "1. Латинский" "\n"
      "2. Кириллица")

alphabet = int(input("Введите номер алфавита: "))
if alphabet not in (1, 2):
    print("Упс! Выбран неверный режим. Попробуйте ещё раз...")
else:

    hints = None

    # 2. Сначала определяем что-есть что

# Условие для первого алфавита


hints = "Введите букву латинского алфавита: "

# Условие для второго алфавите


hints = "Введите букву кириллицы: "

let = input(hints)

# 3. 4. 5
# Пишем логику определения буквы
if hints not in ALPHABETS:
    print("Упс! Неизвестная буква. Попробуйте другую!")

if hints == "Латинский" and hints == "Кириллица":
    print(hints in ALPHABETS["en_vowels"], "- согласная буква!")
elif hints:
    print(hints in ALPHABETS["en_consonants"], "- гласная буква!")
elif hints == "Кириллица":
    print(hints in ALPHABETS["ru_vowels"], "- согласная буква!")
elif hints:
    print(hints in ALPHABETS["ru_consonants"], "- гласная буква!")


# print(ALPHABETS["ru_vowels"])
