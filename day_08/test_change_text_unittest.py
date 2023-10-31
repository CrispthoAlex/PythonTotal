import unittest
import change_text_unittest


class TestingChangeText(unittest.TestCase):

    def test_upper_text(self):
        word = 'good day'
        result = change_text_unittest.change_text(word)

        self.assertEqual(result, 'GOOD DAY')
        self.assertEqual(result, 'Good Day')


"""
    Using upper function / testing text on title format
    -------------------------------------------------------------------
    Ran 1 test in 0.014s

    FAILED (failures=1)

    Good Day != GOOD DAY
    
    Expected :GOOD DAY
    Actual   :Good Day
    <Click to see difference>
    
    Traceback (most recent call last):
      File 'C:\\Users\\Holberton\\CrispthoferRincon\\udemy\\PythonTotal\\day_08\\test_change_text_unittest.py', 
      line 12, in test_upper_text
        self.assertEqual(result, 'Good Day')
    AssertionError: 'GOOD DAY' != 'Good Day'
    - GOOD DAY
    + Good Day
    
    Using title function / testing text on upper format
    -------------------------------------------------------------------
    Ran 1 test in 0.014s

    FAILED (failures=1)

    GOOD DAY != Good Day

    Expected :Good Day
    Actual   :GOOD DAY
    <Click to see difference>
    
    Traceback (most recent call last):
      File 'C:\\Users\\Holberton\\CrispthoferRincon\\udemy\\PythonTotal\\day_08\\test_change_text_unittest.py', 
      line 11, in test_upper_text
        self.assertEqual(result, 'GOOD DAY')
    AssertionError: 'Good Day' != 'GOOD DAY'
    - Good Day
    + GOOD DAY
    
    Using title function / testing text on title format
    -------------------------------------------------------------------
    
    Ran 1 test in 0.003s

    OK
    
    Using upper function / testing text on upper format
    -------------------------------------------------------------------
    
    Ran 1 test in 0.003s

    OK
"""


if __name__ == '__main__':
    unittest.main()

