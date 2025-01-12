import json


def task() -> float:

    filename = "input.json"

    with open(filename) as json_file:  # открываем файл

        json_data = json.load(json_file)  # десериализует строку формата JSON в объект языка Python

    return round(sum([item["score"] * item["weight"] for item in json_data]), 3)


print(task())