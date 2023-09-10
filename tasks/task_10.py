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
    user_input = input("Введите букву: ")
    hints = None

    # hints = "Введите букву кириллицы: "
    # hints = "Введите букву латинского алфавита: "
    #
    # let = input(hints)

# print(ALPHABETS["ru_vowels"])
