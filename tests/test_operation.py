from utils.utils_operation import last_five_operations, operation_executed, parse_operations_data
from tests.test_operations_list import operations

operation = 'tests.operations.json'

def test_operation_executed():
    assert len(operation_executed(operation)) == 3
    print(operation_executed(operation))
    assert operation_executed(operation) == [{'state': 'EXECUTED'},
                                             {'state': 'EXECUTED'},
                                             {'state': 'EXECUTED'}]