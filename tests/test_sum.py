import unittest

from init_stuff import sum

class TestSum(unittest.TestCase):
    def test_list_int(self):
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)
    
    def test_list_int_sad(self):
        data = [1, 2, 3]
        result = sum(data)
        self.assertNotEqual(result, 5)

if __name__ == '__main__':
    unittest.main()