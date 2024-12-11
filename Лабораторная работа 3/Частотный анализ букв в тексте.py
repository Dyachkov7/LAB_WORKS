# Функция для подсчета количества каждой буквы в тексте
def count_letters(text):

    letter_counts = {}
    for char in text.lower():
        if char.isalpha():
            letter_counts[char] = letter_counts.get(char, 0) + 1
    return letter_counts


def calculate_frequency(letter_counts):

    total_letters = sum(letter_counts.values())
    frequency = {letter: round(count / total_letters, 2) for letter, count in letter_counts.items()}
    return frequency

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""
specified_order = [
    'у', 'л', 'к', 'о', 'м', 'р', 'ь', 'я', 'д', 'б', 'з', 'е', 'ё', 'н', 'ы',
    'й', 'а', 'т', 'ц', 'п', 'и', 'ч', 'ю', 'в', 'с', 'х', 'г', 'ш', 'ж', 'щ'
]

letter_counts = count_letters(main_str)

letter_frequency = calculate_frequency(letter_counts)

complete_frequency = {letter: letter_frequency.get(letter, 0.00) for letter in specified_order}

for letter in specified_order:
    print(f"{letter}: {complete_frequency[letter]:.2f}")