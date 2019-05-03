import unittest

from init_stuff import sum

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)
    
    def test_list_int_sad(self):
        """
        Sad case for testing a list of integers sum
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertNotEqual(result, 5)

if __name__ == '__main__':
    unittest.main()