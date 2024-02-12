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
