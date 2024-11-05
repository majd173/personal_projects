import unittest


class TestDifferentMethods(unittest.TestCase):
    """
    This class tests different methods
    """

    def setUp(self):
        """
        This method sets up tests data types
        :return:
        """
        self._list_1 = [1, 2, 3, 4, 5, 6]
        self._data_1 = 2
        self._data_2 = "hello"

    @staticmethod
    def is_even(numbers_list):
        """
        This method checks if the number is even
        """
        return [x for x in numbers_list if x % 2 == 0]

    @staticmethod
    def is_a_string(data):
        """
        This method checks if the data is a string
        :param data:
        """
        return isinstance(data, str)

    def test_is_even(self):
        """
        This method tests if the number is even
        """
        self.assertNotIn(3, self.is_even(self._list_1),
                         "3 is not an even number")

    def test_is_a_string(self):
        """
        This method tests if the data is a string
        :param numeric data type
        """
        self.assertFalse(self.is_a_string(self._data_1), "2 is not a string")

    def test_is_string_2(self):
        """
        This method tests if the data is a string
        :param string data type
        """
        self.assertTrue(self.is_a_string(self._data_2), "hello is a string")
