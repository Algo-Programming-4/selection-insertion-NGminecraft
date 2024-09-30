import sorting
import random
import unittest


class sorting_test(unittest.TestCase):
    def test_sorted(self):
        for _ in range(10):
            nums = [random.randint(1,100) for x in range(random.randint(1,100))]
            result =  sorting.bubble(nums)
            self.assertEqual(result, sorted(nums))
            
    def test_selection(self):
        for _ in range(10):
            nums = [random.randint(1,100) for x in range(random.randint(1,100))]
            result =  sorting.selection(nums)
            self.assertEqual(result, sorted(nums))
      
if __name__ == "__main__":
    test = sorting_test()
    test.test_sorted()
    test.test_selection()
    
