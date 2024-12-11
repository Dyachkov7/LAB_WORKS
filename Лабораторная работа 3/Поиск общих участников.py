# TODO Напишите функцию find_common_participants

def find_common_participants(group1, group2, separator=','):

    list_group1 = group1.split(separator)
    list_group2 = group2.split(separator)
    common_participants = sorted(set(list_group1) & set(list_group2))

    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common = find_common_participants(participants_first_group, participants_second_group, separator='|')

# Выводим результат
print(common)

