import unittest

from tests.test_operations_list import operations

from utils.utils_operation import operation_executed, last_five_operations, parse_operations_data

operation = 'tests.operations.json'


class TestOperations(unittest.TestCase):

    def test_operation_executed(self):
        assert operation_executed(operation) == [{'state': 'EXECUTED'}, {'state': 'EXECUTED'}, {'state': 'EXECUTED'}]
        print(operation_executed(operation))


    def test_last_five_operations(self):
        dates = [elem['date'] for elem in last_five_operations(operations)]
        assert dates == ['2019-11-19T09:22:25.899614',
                         '2019-11-05T12:04:13.781725',
                         '2019-10-30T01:49:52.939296',
                         '2019-08-08T21:58:06.688541',
                         '2019-06-14T19:37:49.044089']