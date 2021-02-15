import unittest

from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Тесты для  'name_function.py'."""
    
    def test_first_last_name(self):
        """ Правда ли имя - фамилия Семен Семенов работают правильно?"""
        formatted_name = get_formatted_name('semen', 'semenov')
        self.assertEqual(formatted_name, 'Semen Semenov')

unittest.main()
