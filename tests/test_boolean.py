import unittest

from init_stuff import istrue

class TestBool(unittest.TestCase):
    def test_boolean(self):
        """
        Tests that things return the correct boolean
        """
        true_or_false = istrue("pls return true")
        self.assertTrue(true_or_false)

    def test_boolean_sad(self):
        """
        Tests that things return the correct boolean, false this time
        """
        true_or_false = istrue("literally not the string that makes this return true")
        self.assertFalse(true_or_false)

if __name__ == '__main__':
    unittest.main()