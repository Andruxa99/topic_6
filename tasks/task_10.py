ALPHABETS: dict = {
    "en_vowels": "AEIOU",
    "en_consonants": "BCDFGHJKLMNPQRSTVWXYZ",
    "ru_vowels": "АЕЁИОУЫЭЮЯ",
    "ru_consonants": "БВГДЖЗЙКЛМНПРСТФХЦЧШЩЪЬ",
}

print("Добро пожаловать в программу \"Буква-Детектив\"!", end="\n\n")
print("Выберите алфавит:""\n"
      "1. Латинский" "\n"
      "2. Кириллица\n")

alphabet: int = int(input("Введите номер алфавита: "))
if alphabet not in (1, 2):
    print("Упс! Выбран неверный режим. Попробуйте ещё раз...")
else:
    hints: None | str = None
    vowels: None | str = None
    consonants: None | str = None
    if alphabet == 1:
        hints = "Введите букву латинского алфавита: "
        vowels = ALPHABETS["en_vowels"]
        consonants = ALPHABETS["en_consonants"]
    else:
        hints = "Введите букву кириллицы: "
        vowels = ALPHABETS["ru_vowels"]
        consonants = ALPHABETS["ru_consonants"]

    let: str = input(hints)
    if let in vowels:
        print(let, "- гласная буква!")
    elif let in consonants:
        print(let, "- согласная буква буква!")
    else:
        print("Упс! Неизвестная буква. Попробуйте другую!")
