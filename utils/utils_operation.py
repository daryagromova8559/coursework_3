import json


def load_operations(filename):
    """
       Загружает список операций из файла

    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


def operation_executed(filename):
    '''Поиск одобренных операций'''
    operation_executed_ = []
    operation_equail = load_operations(filename)
    for i in operation_equail:
        if i.get("state") == "EXECUTED":
            operation_executed_.append(i)
    return operation_executed_


def last_five_operations(operation_executed_):
    '''Вывод последних 5-ти операций'''
    sorted_operations = sorted(operation_executed_, key=lambda x: x["date"], reverse=True)
    last_five = sorted_operations[0:5]
    return last_five
