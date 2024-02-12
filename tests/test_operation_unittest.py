import unittest

from tests.test_operations_list import operations

from utils.utils_operation import operation_executed, last_five_operations, parse_operations_data

operation = 'tests.operations.json'


class TestOperations(unittest.TestCase):

    def test_operation_executed(self):
        assert operation_executed(operation) == [{'state': 'EXECUTED'}, {'state': 'EXECUTED'}, {'state': 'EXECUTED'}]
        print(operation_executed(operation))


