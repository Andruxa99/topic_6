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

    if alphabet == 1:
        hints = "Введите букву латинского алфавита: "

    else:
        hints = "Введите букву кириллицы: "

    let = input(hints)

    if let in ALPHABETS["ru_vowels"]:
        print(let, "- гласная буква!")
    elif let in ALPHABETS["ru_consonants"]:
        print(let, "- согласная буква буква!")
    elif let in ALPHABETS["en_vowels"]:
        print(let, "- гласная буква!")
    elif let in ALPHABETS["en_consonants"]:
        print(let, "- согласная буква")
    else:
        print("Упс! Неизвестная буква. Попробуйте другую!")
